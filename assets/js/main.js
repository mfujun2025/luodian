/* 罗店.cn 共享脚本：导航交互、当前页高亮、页脚年份 */
(function () {
  // 移动端导航开关
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("mainNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.classList.remove("open");
    });
  }

  // 当前页高亮
  var path = location.pathname.replace(/\/$/, "");
  var fileName = path.split("/").pop() || "index.html";
  var links = document.querySelectorAll(".main-nav a");
  links.forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === "/" && fileName === "index.html") a.classList.add("active");
    else if (href && href.indexOf(fileName) !== -1 && fileName !== "index.html") a.classList.add("active");
  });

  // 页脚年份
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
