/* GSIDD IDD tools landscape -- table browser.
   No dependencies; data comes from data/data.js as window.DB. */

(function () {
  'use strict';

  // ---------------------------------------------------------------- config

  var SPLIT_LIST = /\s*[\/,;]\s*/; // for multi-valued facet cells, e.g. "R / C++"

  var CONFIG = {
    tools: {
      blurb: 'Individual software packages of use to the IDD community — simulation and inference ' +
        'models, plus the utilities around them for data access, genomics, surveillance and forecast ' +
        'evaluation. Every entry has been checked against the inclusion criteria, with usage evidence ' +
        'and licence recorded so the basis for inclusion is visible.',
      order: ['Name', 'Description', 'Authors', 'Publication', 'Usage', 'Updated', 'Code',
        'Language', 'Type', 'Pathogen', 'Discipline', 'Licence'],
      hidden: ['Discipline', 'Licence'],
      facets: [
        { col: 'Type' },
        { col: 'Discipline' },
        { col: 'Pathogen' },
        { col: 'Language', split: SPLIT_LIST },
        { col: 'Licence', short: licenceGroup }
      ],
      wide: ['Description', 'Publication'],
      medium: ['Authors'],
      tight: ['Type', 'Discipline', 'Pathogen', 'Language', 'Code', 'Updated', 'Licence'],
      tags: { Type: typeTag, Usage: usageTag }
    },
    ecosystems: {
      blurb: 'Families of tools deliberately built to work together — sharing a core engine, a data ' +
        'structure, a file format, a package registry, or a common design philosophy. The ' +
        '“interoperability basis” column states which of those holds for each entry, so a strong claim ' +
        'is never confused with a weak one. Open a row for the component list and caveats.',
      hidden: ['Anchor tool', 'Interoperability basis', 'Components'],
      facets: [
        { col: 'Language(s)', split: SPLIT_LIST },
        { col: 'Status', short: shortStatus }
      ],
      wide: ['Description', 'Interoperability basis'],
      medium: ['Lead institution(s)'],
      tight: ['Language(s)', 'Anchor tool', 'Components', 'Status', 'Website'],
      tags: { Status: statusTag }
    },
    communities: {
      blurb: 'Networks, consortia, centres, hubs and open-source organisations whose identity is built ' +
        'around IDD software. A research group that happens to have produced a model is not listed; a ' +
        'group whose shared output is a tool, a package suite or a hub standard is.',
      hidden: ['Host / funder', 'Since'],
      facets: [
        { col: 'Type' },
        { col: 'Region / scope', search: true },
        { col: 'Status', short: shortStatus }
      ],
      wide: ['Description', 'Focus', 'Host / funder'],
      tight: ['Type', 'Since', 'Status', 'Website'],
      tags: { Type: typeTag, Status: statusTag }
    }
  };

  // ------------------------------------------------------------- utilities

  function $(id) { return document.getElementById(id); }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  /** Render the small subset of inline markdown the databases actually use. */
  function mdInline(s) {
    return esc(s)
      .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,
        function (m, t, u) { return '<a href="' + u + '" target="_blank" rel="noopener">' + t + '</a>'; })
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^*])\*([^*]+)\*/g, '$1<em>$2</em>');
  }

  function mdBlock(s) {
    return s.split(/\n\s*\n/).map(function (p) {
      p = p.trim();
      if (!p) return '';
      if (/^[-*] /.test(p)) {
        return '<ul>' + p.split('\n').map(function (li) {
          return '<li>' + mdInline(li.replace(/^[-*]\s*/, '')) + '</li>';
        }).join('') + '</ul>';
      }
      return '<p>' + mdInline(p) + '</p>';
    }).join('');
  }

  /** Markdown stripped back to plain text, for searching and sorting. */
  function mdText(s) {
    return s.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[`*]/g, '').trim();
  }

  /** Collapse a verbose status string down to a facetable label. */
  function shortStatus(value) {
    var t = mdText(value);
    if (/caveat/i.test(t)) return 'Active (with caveat)';
    return t.split(/[;,]/)[0].trim() || '—';
  }

  /**
   * Collapse an SPDX identifier to a facetable licence family: versions of the
   * same licence are merged (GPL-2.0 and GPL-3.0 are both "GPL"), families with
   * fewer than five entries are pooled by what they let you do, and anything
   * that is not an open-source licence is kept clearly separate. The table cell
   * still shows the exact identifier.
   */
  function licenceGroup(value) {
    var t = mdText(value).toLowerCase();
    if (/^mit\b/.test(t)) return 'MIT';
    if (/^gpl/.test(t)) return 'GPL';
    if (/^bsd/.test(t)) return 'BSD';
    if (/^(lgpl|agpl|eupl|mpl|cecill)/.test(t)) return 'Other copyleft';
    if (/^(apache|artistic|isc|zlib|unlicense|cc0)|public domain/.test(t)) return 'Other permissive';
    if (/not stated|unknown|unlicensed/.test(t)) return 'Not stated';
    return 'Proprietary or closed';
  }

  function typeTag(value) {
    var t = mdText(value).toLowerCase();
    if (t === 'model') return 'tag-model';
    if (t === 'utility') return 'tag-utility';
    if (t.indexOf('ai') === 0) return 'tag-ai';
    return '';
  }

  /**
   * The Usage cell is a label plus the evidence behind it, so only the label
   * becomes a chip: returning an object rather than a class name tells the
   * renderer to keep the rest of the cell as text after it.
   */
  function usageTag(value) {
    var match = /^(Established|Emerging|Minimal)\s*(?:\(([\s\S]*)\))?$/.exec(mdText(value));
    if (!match) return '';
    return { cls: 'tag-usage-' + match[1].toLowerCase(), label: match[1], rest: match[2] || '' };
  }

  function statusTag(value) {
    var t = mdText(value).toLowerCase();
    if (/dormant|retired|archived|inactive/.test(t)) return 'tag-inactive';
    if (/caveat|maintenance|no longer/.test(t)) return 'tag-caveat';
    if (/active/.test(t)) return 'tag-active';
    return '';
  }

  // The Usage column leads with an ordinal label, which has to sort by rank
  // rather than by spelling: descending is Established, Emerging, Minimal.
  var USAGE_RANK = { established: 3, emerging: 2, minimal: 1 };

  function usageRank(text) {
    return USAGE_RANK[String(text).split(/[\s(]/)[0].toLowerCase()] || 0;
  }

  function compare(a, b) {
    var na = parseFloat(a), nb = parseFloat(b);
    if (!isNaN(na) && !isNaN(nb) && /^[~<>]?[\d.,]+$/.test(a) && /^[~<>]?[\d.,]+$/.test(b)) return na - nb;
    return a.toLowerCase().localeCompare(b.toLowerCase(), 'en');
  }

  /** Wrap search-term matches in <mark>, walking text nodes so markup is left alone. */
  function highlight(root, query) {
    if (!query) return;
    var re = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    var nodes = [], node;
    while ((node = walker.nextNode())) if (re.test(node.nodeValue)) nodes.push(node);
    nodes.forEach(function (n) {
      var span = el('span');
      span.innerHTML = esc(n.nodeValue).replace(re, '<mark>$1</mark>');
      n.parentNode.replaceChild(span, n);
    });
  }

  // ----------------------------------------------------------- data model

  var sections = {}; // key -> prepared section
  var order = [];
  var current = null;

  /**
   * Reorder a section's columns (and every row's cells to match) to `cfg.order`.
   * Names not listed keep their source order, on the end; names that no longer
   * exist in the data are ignored, so the config can never drop a column.
   */
  function applyOrder(raw, wanted) {
    var listed = wanted.filter(function (c) { return raw.columns.indexOf(c) !== -1; });
    var rest = raw.columns.filter(function (c) { return listed.indexOf(c) === -1; });
    var columns = listed.concat(rest);
    var idx = columns.map(function (c) { return raw.columns.indexOf(c); });
    raw.columns = columns;
    raw.rows = raw.rows.map(function (cells) {
      return idx.map(function (i) { return cells[i]; });
    });
  }

  window.DB.sections.forEach(function (raw) {
    var cfg = CONFIG[raw.key] || {};
    if (cfg.order) applyOrder(raw, cfg.order);
    var section = {
      key: raw.key,
      label: raw.label,
      source: raw.source,
      intro: cfg.blurb || mdText(raw.intro),
      columns: raw.columns,
      defaultColumns: raw.columns.slice(),  // what the Reset button goes back to
      details: raw.details || {},
      cfg: cfg,
      // per-row cache: raw cells plus a lowercase blob for free-text search
      rows: raw.rows.map(function (cells, i) {
        return { i: i, cells: cells, text: cells.map(mdText).join('   ').toLowerCase() };
      }),
      state: {
        query: '',
        filters: {},          // column -> Set of selected values
        visible: {},          // column -> bool
        sortCol: 0,
        sortDir: 1
      }
    };
    section.columns.forEach(function (col) {
      section.state.visible[col] = (cfg.hidden || []).indexOf(col) === -1;
    });
    (cfg.facets || []).forEach(function (f) { section.state.filters[f.col] = new Set(); });
    sections[raw.key] = section;
    order.push(raw.key);
  });

  /**
   * Move a column, dragging every row's cells along with it, so the rest of the
   * code can go on treating a column's position as its index. The first column
   * is the record's identity — it stays put, and nothing moves in front of it.
   */
  function setColumnOrder(section, wanted) {
    var sorted = section.columns[section.state.sortCol];
    var index = wanted.map(function (col) { return section.columns.indexOf(col); });
    section.columns = wanted.slice();
    section.rows.forEach(function (row) {
      row.cells = index.map(function (i) { return row.cells[i]; });
    });
    // the sort is on a column, not on a position, so follow it to its new index
    section.state.sortCol = Math.max(0, section.columns.indexOf(sorted));
    columnsBuiltFor = null;  // the picker lists columns in table order
  }

  function moveColumn(section, from, to) {
    to = Math.max(1, Math.min(section.columns.length - 1, to));
    if (from < 1 || from === to) return false;
    var wanted = section.columns.slice();
    wanted.splice(to, 0, wanted.splice(from, 1)[0]);
    setColumnOrder(section, wanted);
    return true;
  }

  /** Value(s) a row contributes to a facet. */
  function facetValues(section, facet, row) {
    var v = row.cells[section.columns.indexOf(facet.col)] || '';
    if (facet.short) return [facet.short(v)];
    var t = mdText(v);
    if (!t) return ['—'];
    if (facet.split) return t.split(facet.split).map(function (s) { return s.trim(); }).filter(Boolean);
    return [t];
  }

  function matchesFacet(section, facet, row) {
    var selected = section.state.filters[facet.col];
    if (!selected.size) return true;
    return facetValues(section, facet, row).some(function (v) { return selected.has(v); });
  }

  /** Rows passing every filter; `except` skips one facet, for facet-count maths. */
  function filterRows(section, except) {
    var q = section.state.query.trim().toLowerCase();
    var facets = section.cfg.facets || [];
    return section.rows.filter(function (row) {
      if (q && row.text.indexOf(q) === -1) return false;
      for (var i = 0; i < facets.length; i++) {
        if (facets[i] === except) continue;
        if (!matchesFacet(section, facets[i], row)) return false;
      }
      return true;
    });
  }

  /** A cell saying nothing: no value, an em dash, or a date we could not establish. */
  function isBlank(value) {
    return !value || value === '—' || value.toUpperCase() === 'N/A';
  }

  function sortRows(section, rows) {
    var idx = section.state.sortCol, dir = section.state.sortDir;
    return rows.slice().sort(function (a, b) {
      var x = mdText(a.cells[idx] || ''), y = mdText(b.cells[idx] || '');
      // blanks are the absence of an answer rather than the smallest one, so they
      // sink to the bottom whichever way the column is sorted
      if (isBlank(x) !== isBlank(y)) return isBlank(x) ? 1 : -1;
      if (section.columns[idx] === 'Usage') {
        var rx = usageRank(x), ry = usageRank(y);
        // Rank alone: within a label the evidence strings are not comparable
        // with each other, so ties keep the table's own alphabetical order.
        if (rx || ry) return dir * (rx - ry);
      }
      return dir * compare(x, y);
    });
  }

  function activeFilterCount(section) {
    var n = section.state.query.trim() ? 1 : 0;
    Object.keys(section.state.filters).forEach(function (k) { n += section.state.filters[k].size; });
    return n;
  }

  // -------------------------------------------------------------- rendering

  function renderTabs() {
    var nav = document.querySelector('.tabs');
    nav.innerHTML = '';
    order.forEach(function (key) {
      var section = sections[key];
      var btn = el('button', 'tab');
      btn.type = 'button';
      btn.setAttribute('role', 'tab');
      btn.setAttribute('aria-selected', key === current ? 'true' : 'false');
      btn.appendChild(document.createTextNode(section.label));
      btn.appendChild(el('span', 'tab-count', String(section.rows.length)));
      btn.addEventListener('click', function () { selectTab(key); });
      nav.appendChild(btn);
    });
  }

  var openFacet = null;   // facet column whose dropdown is open, so it survives a re-render
  var facetScroll = 0;

  /** Stable option order for a facet: by overall frequency, computed once per section. */
  function facetOrder(section, facet) {
    if (!facet._order) {
      var totals = {};
      section.rows.forEach(function (row) {
        facetValues(section, facet, row).forEach(function (v) { totals[v] = (totals[v] || 0) + 1; });
      });
      facet._order = Object.keys(totals).sort(function (a, b) {
        return totals[b] - totals[a] || compare(a, b);
      });
    }
    return facet._order;
  }

  function renderFacets() {
    var section = sections[current];
    var host = $('facets');
    host.innerHTML = '';
    (section.cfg.facets || []).forEach(function (facet) {
      // counts computed against the other filters, so the numbers stay meaningful
      var pool = filterRows(section, facet);
      var counts = {};
      pool.forEach(function (row) {
        facetValues(section, facet, row).forEach(function (v) { counts[v] = (counts[v] || 0) + 1; });
      });
      var selected = section.state.filters[facet.col];
      var values = facetOrder(section, facet);

      var wrap = el('div', 'dropdown');
      var btn = el('button', 'btn' + (selected.size ? ' is-active' : ''));
      btn.type = 'button';
      btn.setAttribute('data-dropdown-toggle', '');
      btn.setAttribute('aria-expanded', 'false');
      btn.dataset.facet = facet.col;
      btn.appendChild(document.createTextNode(facet.col));
      if (selected.size) btn.appendChild(el('span', 'badge', String(selected.size)));
      btn.appendChild(el('span', 'caret'));
      wrap.appendChild(btn);

      var panel = el('div', 'dropdown-panel');
      panel.setAttribute('data-dropdown-panel', '');
      panel.hidden = true;

      var head = el('div', 'dropdown-head');
      head.appendChild(el('strong', null, facet.col));
      var clear = el('button', 'link-btn', 'Clear');
      clear.type = 'button';
      clear.addEventListener('click', function () { selected.clear(); refresh(); });
      head.appendChild(clear);
      panel.appendChild(head);

      var list = el('div', 'dropdown-list');
      if (facet.search) {
        var box = el('input', 'dropdown-search');
        box.type = 'search';
        box.placeholder = 'Filter options…';
        box.addEventListener('input', function () {
          var q = box.value.toLowerCase();
          Array.prototype.forEach.call(list.children, function (opt) {
            opt.hidden = opt.textContent.toLowerCase().indexOf(q) === -1;
          });
        });
        box.addEventListener('click', function (e) { e.stopPropagation(); });
        panel.appendChild(box);
      }

      values.forEach(function (value) {
        var count = counts[value] || 0;
        var opt = el('label', 'opt');
        var cb = el('input');
        cb.type = 'checkbox';
        cb.checked = selected.has(value);
        cb.addEventListener('change', function () {
          if (cb.checked) selected.add(value); else selected.delete(value);
          facetScroll = list.scrollTop;
          refresh();
        });
        // an option that can no longer match anything is dimmed, not removed
        if (!count && !cb.checked) opt.className += ' is-empty';
        opt.appendChild(cb);
        opt.appendChild(el('span', 'opt-label', value));
        opt.appendChild(el('span', 'opt-count', String(count)));
        list.appendChild(opt);
      });
      panel.appendChild(list);
      wrap.appendChild(panel);
      host.appendChild(wrap);

      if (openFacet === facet.col) {
        panel.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
        list.scrollTop = facetScroll;
      }
    });
  }

  var columnsBuiltFor = null;

  function renderColumnPicker() {
    var section = sections[current];
    var list = $('columns-list');

    // Build once per section, then only update state -- rebuilding on every toggle
    // would replace the checkbox the user is mid-click on.
    if (columnsBuiltFor !== current) {
      list.innerHTML = '';
      section.columns.forEach(function (col, i) {
        var opt = el('label', 'opt');
        var cb = el('input');
        cb.type = 'checkbox';
        cb.addEventListener('change', function () {
          section.state.visible[col] = cb.checked;
          refresh();
        });
        opt.appendChild(cb);
        opt.appendChild(el('span', 'opt-label', col));
        opt.dataset.index = String(i);
        list.appendChild(opt);
      });
      columnsBuiltFor = current;
    }

    var shown = section.columns.filter(function (c) { return section.state.visible[c]; });
    Array.prototype.forEach.call(list.children, function (opt, i) {
      var cb = opt.querySelector('input');
      cb.checked = section.state.visible[section.columns[i]];
      // keep the identifying first column pinned, and never let the last one go
      var locked = i === 0 || (cb.checked && shown.length === 1);
      cb.disabled = locked;
      opt.classList.toggle('is-locked', locked);
    });

    var hiddenCount = section.columns.length - shown.length;
    $('columns-badge').textContent = hiddenCount ? String(hiddenCount) + ' hidden' : '';
  }

  function renderChips() {
    var section = sections[current];
    var host = $('active-filters');
    host.innerHTML = '';
    Object.keys(section.state.filters).forEach(function (col) {
      section.state.filters[col].forEach(function (value) {
        var chip = el('span', 'chip');
        chip.appendChild(el('b', null, col + ':'));
        chip.appendChild(document.createTextNode(' ' + value));
        var x = el('button', null, '×');
        x.type = 'button';
        x.setAttribute('aria-label', 'Remove filter ' + col + ' ' + value);
        x.addEventListener('click', function () {
          section.state.filters[col].delete(value);
          refresh();
        });
        chip.appendChild(x);
        host.appendChild(chip);
      });
    });
  }

  function cellClass(section, col, index) {
    var classes = [];
    if (index === 0) classes.push('col-sticky', 'cell-name');
    if ((section.cfg.wide || []).indexOf(col) !== -1) classes.push('cell-wide');
    if ((section.cfg.medium || []).indexOf(col) !== -1) classes.push('cell-medium');
    if ((section.cfg.tight || []).indexOf(col) !== -1) classes.push('cell-tight');
    return classes.join(' ');
  }

  var dragFrom = null;  // index of the column being dragged, across re-renders

  function clearDropMarks() {
    document.querySelectorAll('#table-head th').forEach(function (th) {
      th.classList.remove('drop-before', 'drop-after');
    });
  }

  /** Put focus back on a column's header, so a keyboard move can be repeated. */
  function focusHeader(col) {
    var th = document.querySelector('#table-head th[data-column="' + col.replace(/"/g, '\\"') + '"]');
    if (th) th.querySelector('button').focus();
  }

  function renderTable(rows) {
    var section = sections[current];
    var head = $('table-head');
    var body = $('table-body');
    head.innerHTML = '';
    body.innerHTML = '';

    var cols = section.columns
      .map(function (col, i) { return { col: col, i: i }; })
      .filter(function (c) { return section.state.visible[c.col]; });

    cols.forEach(function (c, position) {
      var th = el('th', cellClass(section, c.col, position));
      var movable = c.i > 0;
      if (movable) {
        th.draggable = true;
        th.title = 'Drag to reorder, or Alt + ← / → from the keyboard';
      }
      th.dataset.column = c.col;
      var btn = el('button');
      btn.type = 'button';
      btn.appendChild(document.createTextNode(c.col));
      var arrow = el('span', 'sort-arrow',
        section.state.sortCol === c.i ? (section.state.sortDir > 0 ? '▲' : '▼') : '▴▾');
      btn.appendChild(arrow);
      if (section.state.sortCol === c.i) {
        th.setAttribute('aria-sort', section.state.sortDir > 0 ? 'ascending' : 'descending');
      }
      btn.addEventListener('click', function () {
        if (section.state.sortCol === c.i) section.state.sortDir *= -1;
        else { section.state.sortCol = c.i; section.state.sortDir = 1; }
        refresh();
      });

      // Alt + arrow does by keyboard what dragging does by mouse: swap with the
      // neighbouring visible column, hidden columns in between coming along.
      btn.addEventListener('keydown', function (e) {
        if (!e.altKey || (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight')) return;
        var neighbour = cols[position + (e.key === 'ArrowLeft' ? -1 : 1)];
        if (!neighbour || !movable) return;
        e.preventDefault();
        if (moveColumn(section, c.i, neighbour.i)) {
          refresh();
          focusHeader(c.col);
        }
      });

      if (movable) {
        th.addEventListener('dragstart', function (e) {
          dragFrom = c.i;
          e.dataTransfer.effectAllowed = 'move';
          e.dataTransfer.setData('text/plain', c.col); // Firefox needs some payload
          th.classList.add('is-dragging');
        });
        th.addEventListener('dragend', function () {
          dragFrom = null;
          clearDropMarks();
          th.classList.remove('is-dragging');
        });
      }
      th.addEventListener('dragover', function (e) {
        if (dragFrom === null || dragFrom === c.i || c.i === 0) return;
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
        clearDropMarks();
        th.classList.add(dragFrom < c.i ? 'drop-after' : 'drop-before');
      });
      th.addEventListener('drop', function (e) {
        if (dragFrom === null) return;
        e.preventDefault();
        var from = dragFrom;
        dragFrom = null;
        clearDropMarks();
        if (moveColumn(section, from, c.i)) refresh();
      });

      th.appendChild(btn);
      head.appendChild(th);
    });

    var query = section.state.query.trim();
    rows.forEach(function (row) {
      var tr = el('tr');
      tr.tabIndex = 0;
      cols.forEach(function (c, position) {
        var td = el('td', cellClass(section, c.col, position));
        var value = row.cells[c.i] || '';
        var tagFn = (section.cfg.tags || {})[c.col];
        var spec = tagFn && value ? tagFn(value) : null;
        if (spec && typeof spec === 'object') {
          td.appendChild(el('span', 'tag ' + spec.cls, spec.label));
          if (spec.rest) {
            var rest = el('span', 'tag-note');
            rest.innerHTML = mdInline(spec.rest);
            td.appendChild(rest);
          }
        } else if (tagFn && value) {
          var facet = (section.cfg.facets || []).filter(function (f) { return f.col === c.col; })[0];
          var label = facet && facet.short ? facet.short(value) : mdText(value);
          var tag = el('span', 'tag ' + spec, label);
          if (label !== mdText(value)) tag.title = mdText(value);
          td.appendChild(tag);
        } else {
          td.innerHTML = mdInline(value);
        }
        highlight(td, query);
        tr.appendChild(td);
      });
      tr.addEventListener('click', function (e) {
        if (e.target.closest('a')) return; // let links behave like links
        openDrawer(row);
      });
      tr.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') openDrawer(row);
      });
      body.appendChild(tr);
    });

    $('empty').hidden = rows.length > 0;
    $('table').hidden = rows.length === 0;
  }

  function refresh() {
    var section = sections[current];
    var rows = sortRows(section, filterRows(section));

    $('tab-intro').textContent = section.intro;
    $('source-note').innerHTML = 'Source: <code>' + esc(section.source) +
      '</code> · ' + section.rows.length + ' entries · click any row for the full record.';

    renderFacets();
    renderColumnPicker();
    renderChips();
    renderTable(rows);

    var count = $('result-count');
    count.innerHTML = rows.length === section.rows.length
      ? 'Showing all <strong>' + section.rows.length + '</strong> ' + section.label.toLowerCase()
      : 'Showing <strong>' + rows.length + '</strong> of ' + section.rows.length + ' ' + section.label.toLowerCase();
    $('clear-all').hidden = activeFilterCount(section) === 0;

    if ($('search').value !== section.state.query) $('search').value = section.state.query;
  }

  function selectTab(key) {
    current = key;
    if (location.hash.slice(1) !== key) history.replaceState(null, '', '#' + key);
    document.querySelectorAll('.tab').forEach(function (tab, i) {
      tab.setAttribute('aria-selected', order[i] === key ? 'true' : 'false');
    });
    closeDropdowns();
    refresh();
  }

  // ---------------------------------------------------------------- drawer

  function openDrawer(row) {
    var section = sections[current];
    var name = mdText(row.cells[0]);
    $('drawer-title').textContent = name;

    var body = $('drawer-body');
    body.innerHTML = '';
    section.columns.forEach(function (col, i) {
      if (i === 0) return;
      var value = row.cells[i] || '';
      if (!value || value === '—') return;
      var field = el('div', 'field');
      field.appendChild(el('div', 'field-label', col));
      var v = el('div', 'field-value');
      v.innerHTML = mdInline(value);
      field.appendChild(v);
      body.appendChild(field);
    });

    var detail = section.details[name];
    if (detail) {
      var block = el('div', 'detail-block');
      block.appendChild(el('h3', null, 'Detail'));
      var inner = el('div');
      inner.innerHTML = mdBlock(detail);
      block.appendChild(inner);
      body.appendChild(block);
    }

    $('drawer').hidden = false;
    $('drawer-scrim').hidden = false;
    $('drawer-close').focus();
  }

  function closeDrawer() {
    $('drawer').hidden = true;
    $('drawer-scrim').hidden = true;
  }

  // ------------------------------------------------------------- dropdowns

  function closeDropdowns() {
    openFacet = null;
    facetScroll = 0;
    document.querySelectorAll('[data-dropdown-panel]').forEach(function (panel) {
      panel.hidden = true;
      var toggle = panel.parentNode.querySelector('[data-dropdown-toggle]');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    });
  }

  document.addEventListener('click', function (e) {
    var toggle = e.target.closest('[data-dropdown-toggle]');
    if (toggle) {
      var panel = toggle.parentNode.querySelector('[data-dropdown-panel]');
      var wasOpen = !panel.hidden;
      closeDropdowns();
      if (!wasOpen) {
        panel.hidden = false;
        toggle.setAttribute('aria-expanded', 'true');
        openFacet = toggle.dataset.facet || null;
        // flip the panel if it would run off the right edge
        var rect = panel.getBoundingClientRect();
        if (rect.right > window.innerWidth - 12) panel.classList.add('align-right');
      }
      return;
    }
    if (!e.target.closest('[data-dropdown-panel]')) closeDropdowns();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeDropdowns(); closeDrawer(); }
  });

  // ------------------------------------------------------------------ CSV

  function downloadCsv() {
    var section = sections[current];
    var cols = section.columns.filter(function (c) { return section.state.visible[c]; });
    var idx = cols.map(function (c) { return section.columns.indexOf(c); });
    var rows = sortRows(section, filterRows(section));
    var lines = [cols].concat(rows.map(function (row) {
      return idx.map(function (i) { return row.cells[i] || ''; });
    }));
    var csv = lines.map(function (line) {
      return line.map(function (cell) { return '"' + String(cell).replace(/"/g, '""') + '"'; }).join(',');
    }).join('\n');

    var blob = new Blob(['﻿' + csv], { type: 'text/csv;charset=utf-8' });
    var link = el('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'gsidd-' + section.key + '.csv';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
  }

  // ------------------------------------------------------------------ wire

  var searchTimer;
  $('search').addEventListener('input', function (e) {
    clearTimeout(searchTimer);
    var value = e.target.value;
    searchTimer = setTimeout(function () {
      sections[current].state.query = value;
      refresh();
    }, 130);
  });

  $('clear-all').addEventListener('click', function () {
    var state = sections[current].state;
    state.query = '';
    $('search').value = '';
    Object.keys(state.filters).forEach(function (k) { state.filters[k].clear(); });
    refresh();
  });

  $('columns-reset').addEventListener('click', function () {
    var section = sections[current];
    setColumnOrder(section, section.defaultColumns);
    section.columns.forEach(function (col) {
      section.state.visible[col] = (section.cfg.hidden || []).indexOf(col) === -1;
    });
    refresh();
  });

  $('download').addEventListener('click', downloadCsv);
  $('drawer-close').addEventListener('click', closeDrawer);
  $('drawer-scrim').addEventListener('click', closeDrawer);

  window.addEventListener('hashchange', function () {
    var key = location.hash.slice(1);
    if (sections[key] && key !== current) selectTab(key);
  });

  current = sections[location.hash.slice(1)] ? location.hash.slice(1) : order[0];
  renderTabs();
  selectTab(current);
})();
