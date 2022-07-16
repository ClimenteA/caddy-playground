const container = document.getElementById("app")

let state = {}


function login() {

    m.request({
        method: "POST",
        url: "/api/discovery-service/register",
        body: {
            "url": "",
            "token": "secret-token",
            "app": "frontend-service",
            "meta": {}
        },
    })
        .then(data => {
            state["token"] = data.token
        })

}



function authData() {

    m.request({
        method: "GET",
        url: "/api/auth-service/data",
    })
        .then(data => {
            console.log(data)
        })

}


function renderData() {
    return {
        oninit: () => {
            login()
            authData()
        },
        view: () => [


        ]
    }
}


m.mount(container, renderData())