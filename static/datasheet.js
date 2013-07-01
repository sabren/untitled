/*

 This is a basic editable data grid, powered by YUI and the inline enhancements here:
 http://stlsmiths.github.io/blunderalong/dt_cellinline.html

 */

$yui = YUI();

$yui.add('datasheet',
    function (Y) {
        if (! Y.datasheet) {
            Y.datasheet = {
                table: new Y.DataTable({
                    columns: [
                        { key: "id", label: '#', editable: false },
                        { key: "name", editor: 'inline' },
                        "price"
                    ],
                    data: [
                        { id: "ga_3475", name: "gadget", price: "$6.99" },
                        { id: "sp_9980", name: "sprocket", price: "$3.75" },
                        { id: "wi_0650", name: "widget", price: "$4.25" }
                    ],
                    summary: "Price sheet for inventory parts",
                    caption: "Example table with simple columns",
                    sortable: ["id", "name", "price"],
                    editable: true,
                    editOpenType: 'click',
                    defaultEditor: 'inline'
                }),
                counter: 0
            };
           Y.datasheet.table.render("#simple")
        }
    },
    '0.0.1',
    {
        requires: [
            "datatable", 'gallery-datatable-celleditor-inline',
            "gallery-datatable-formatters", 'autocomplete-plugin'
        ]
    });

function addRow() {
    $yui.use('datasheet', function (Y) {
        Y.datasheet.table.addRow({ id: "dyn_" + Y.datasheet.counter++, name: "", price: "" })
    });
}
