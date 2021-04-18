document.addEventListener("DOMContentLoaded", async (event) => {
  const table = document.getElementById("table");

  const courses = await fetchCourses();

  const tbody = mountTableBody(courses);
  table.querySelector('tbody').remove();
  table.appendChild(tbody);
});

function fetchCourses() {
  return fetch(`${window.location.href}assets/output.json`).then((r) =>
    r.json()
  );
}

function mountTableBody(courses) {
  const tbody = document.createElement("tbody");
  tbody.classList = 'text-gray-600 text-sm font-light';
  courses.forEach(({ name }, i) => {
    const tr = document.createElement("tr");
    tr.classList = 'border-b border-gray-200 bg-gray-50 hover:bg-gray-100'
    const tdId = document.createElement("td");
    tdId.classList = 'py-3 px-6 text-left'
    tdId.textContent = i + 1;
    const tdName = document.createElement("td");
    tdName.textContent = name;
    tdName.classList = 'py-3 px-6 text-left'
    tr.appendChild(tdId);
    tr.appendChild(tdName);

    tbody.appendChild(tr);
  });
  return tbody;
}
