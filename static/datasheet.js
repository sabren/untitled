

YUI().use("datatable", function (Y) {

  // A table from data with keys that work fine as column names
  var simple = new Y.DataTable({
    columns: ["id", "name", "price"],
    data   : [
      { id: "ga_3475", name: "gadget",   price: "$6.99" },
      { id: "sp_9980", name: "sprocket", price: "$3.75" },
      { id: "wi_0650", name: "widget",   price: "$4.25" }
    ],
    summary: "Price sheet for inventory parts",
    caption: "Example table with simple columns",
    sortable: ["id", "name", "price"],
    className:"pure-table-horizontal"
  });

  simple.render("#simple" );

});
