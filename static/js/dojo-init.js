var dojoConfig = {
    baseUrl: "/static/",
    tlmSiblingOfDojo: false,
    packages: [
        { name: "dojo", location: "lib/dojo" },
        { name: "dijit", location: "lib/dijit" },
        { name: "dojox", location: "lib/dojox" },
        { name: "my", location: "my", main: "app" }
    ]
};
require([ "/static/js/minrelite-dojo.js" ]);
