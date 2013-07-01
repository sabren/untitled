/*
 This is a basic editable data grid, powered by YUI and the inline enhancements here:
 http://stlsmiths.github.io/blunderalong/dt_cellinline.html
 */

YUI({ gallery: 'gallery-2013.01.16-21-05'}).use(
    "datatable", 'gallery-datatable-celleditor-inline',
    "gallery-datatable-formatters",'autocomplete-plugin',
function (Y) {

  // A table from data with keys that work fine as column names
  var simple = new Y.DataTable({
    columns: [
      { key: "id", label:'#', editable:false },
      { key: "name", editor:'inline' },
      "price" ],
    data   : [
      { id: "ga_3475", name: "gadget",   price: "$6.99" },
      { id: "sp_9980", name: "sprocket", price: "$3.75" },
      { id: "wi_0650", name: "widget",   price: "$4.25" }
    ],
    summary: "Price sheet for inventory parts",
    caption: "Example table with simple columns",
    sortable: ["id", "name", "price"],
    editable:true,
    editOpenType: 'click',
    defaultEditor: 'inline'
  });

  simple.render("#simple" );

});
