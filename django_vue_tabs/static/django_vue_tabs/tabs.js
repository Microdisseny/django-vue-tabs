var add_tabs = function (selector) {
  var Tabs = vuetabs.Tabs;
  var Tab = vuetabs.Tab;
  var app = new Vue({
      el: selector,
      components: {
        tabs: Tabs,
        tab: Tab
      }
  });
};
