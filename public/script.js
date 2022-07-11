

const container = document.getElementById("app")






function renderData() {
    return {
        view: () => m("p", "Page loaded")
    }
}


m.mount(container, renderData())