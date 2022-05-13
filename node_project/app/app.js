(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "preact", "preact"], factory);
    }
})(function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var React = require("preact");
    var ReactDOM = require("preact");
    ReactDOM.render(React.createElement("h2", null, "Hello, world!"), document.body);
});
//# sourceMappingURL=app.js.map