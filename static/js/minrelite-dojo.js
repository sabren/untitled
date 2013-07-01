
define(["dojo/store/Memory"],
function(Memory){

    var employees = [
        {name:"Jim", department:"accounting"},
        {name:"Bill", department:"engineering"},
        {name:"Mike", department:"sales"},
        {name:"John", department:"sales"}
    ];
    var employeeStore = new Memory({data:employees, idProperty: "name"});
    employeeStore.query({department:"sales"}).forEach(function(employee){
        // this is called for each employee in the sales department
        // alert(employee.name);
    });


});

require(["dojo/store/JsonRest"],
function(JsonRest){
    var employeeStore = new JsonRest({target:"/Employee/"});
    employeeStore.get("Bill").then(function(bill){
        // called once Bill was retrieved
    });
});



require([
    "dojo/_base/declare", "dgrid/OnDemandGrid","dgrid/editor", "dgrid/Keyboard", "dgrid/Selection",
    "minrelite-dojo"
], function(declare, OnDemandGrid, editor, Keyboard, Selection, minrelite){
    var editGrid = new (declare([OnDemandGrid, Keyboard, Selection]))({
        store: minrelite.store,
        columns: [
            editor({
                label: "Name",
                field: "name",
                editor: "text",
                editOn: "dblclick"
            })
            // ...
        ]
    }, "editGrid");
});

