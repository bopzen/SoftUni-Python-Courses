function solve(browser, actions) {
    for (const action of actions) {
        if (action === "Clear History and Cache") {
            browser["Open Tabs"] = [];
            browser["Recently Closed"] = [];
            browser["Browser Logs"] = [];
            continue;
        }
        let [actionType, website] = action.split(" ");
        if (actionType === "Open") {
            browser["Open Tabs"].push(website);
            browser["Browser Logs"].push(action);
        } else if (actionType === "Close") {
            if (browser["Open Tabs"].includes(website)) {
                browser["Open Tabs"].splice(browser["Open Tabs"].indexOf(website), 1);
                browser["Recently Closed"].push(website);
                browser["Browser Logs"].push(action);
            }
        }
    }
    console.log(browser["Browser Name"]);
    console.log(`Open Tabs: ${browser["Open Tabs"].join(", ")}`);
    console.log(`Recently Closed: ${browser["Recently Closed"].join(", ")}`);
    console.log(`Browser Logs: ${browser["Browser Logs"].join(", ")}`);
}

solve({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
"Recently Closed":["Yahoo","Gmail"],
"Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
["Close Facebook", "Open StackOverFlow", "Open Google"]
);
solve({"Browser Name":"Mozilla Firefox",
"Open Tabs":["YouTube"],
"Recently Closed":["Gmail", "Dropbox"],
"Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
);