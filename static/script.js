// AI for Gig Workers — static site script
(function () {
  "use strict";

  // Simple shift adder for the timesheet page.
  function addShift() {
    var table = document.getElementById("shifts");
    if (!table) return;

    var date = document.getElementById("shift-date");
    var start = document.getElementById("shift-start");
    var end = document.getElementById("shift-end");
    var rate = document.getElementById("shift-rate");
    var tbody = table.querySelector("tbody");

    if (!date || !start || !end || !rate || !tbody) return;
    if (!date.value || !start.value || !end.value || !rate.value) {
      alert("Please fill in all fields before adding a shift.");
      return;
    }

    var hours = computeHours(start.value, end.value);
    var total = (hours * parseFloat(rate.value)).toFixed(2);

    var row = document.createElement("tr");
    row.innerHTML =
      "<td>" + escapeHtml(date.value) + "</td>" +
      "<td>" + escapeHtml(start.value) + "</td>" +
      "<td>" + escapeHtml(end.value) + "</td>" +
      "<td>" + escapeHtml(hours.toFixed(2)) + "</td>" +
      "<td>$" + escapeHtml(rate.value) + "</td>" +
      "<td>$" + escapeHtml(total) + "</td>" +
      "<td><button type=\"button\" class=\"remove\">Remove</button></td>";

    tbody.appendChild(row);
    updateTotals(tbody);

    date.value = "";
    start.value = "";
    end.value = "";
    rate.value = "";
    date.focus();
  }

  function computeHours(start, end) {
    var s = parseTime(start);
    var e = parseTime(end);
    if (s === null || e === null) return 0;
    var diff = e - s;
    if (diff < 0) diff += 24 * 60 * 60 * 1000; // overnight shift
    return diff / (1000 * 60 * 60);
  }

  function parseTime(value) {
    var parts = value.split(":");
    if (parts.length !== 2) return null;
    var h = parseInt(parts[0], 10);
    var m = parseInt(parts[1], 10);
    if (isNaN(h) || isNaN(m) || h < 0 || h > 23 || m < 0 || m > 59) return null;
    var d = new Date();
    d.setHours(h, m, 0, 0);
    return d.getTime();
  }

  function updateTotals(tbody) {
    var totalHours = 0;
    var totalPay = 0;
    var rows = tbody.querySelectorAll("tr");
    for (var i = 0; i < rows.length; i++) {
      var cells = rows[i].querySelectorAll("td");
      if (cells.length >= 6) {
        totalHours += parseFloat(cells[3].textContent) || 0;
        totalPay += parseFloat(cells[5].textContent.replace("$", "")) || 0;
      }
    }
    var el = document.getElementById("total-hours");
    if (el) el.textContent = totalHours.toFixed(2);
    el = document.getElementById("total-pay");
    if (el) el.textContent = "$" + totalPay.toFixed(2);
  }

  function escapeHtml(text) {
    var div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  function init() {
    var btn = document.getElementById("add-shift");
    if (btn) btn.addEventListener("click", addShift);

    document.body.addEventListener("click", function (e) {
      if (e.target && e.target.classList.contains("remove")) {
        var row = e.target.closest("tr");
        if (row) {
          row.remove();
          var tbody = document.querySelector("#shifts tbody");
          if (tbody) updateTotals(tbody);
        }
      }
    });

    var printBtn = document.getElementById("print-sheet");
    if (printBtn) {
      printBtn.addEventListener("click", function () { window.print(); });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
