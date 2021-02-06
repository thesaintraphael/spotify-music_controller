import React, { Component } from 'react';
import { render } from 'react-dom';
import HomePage from "./HomePage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

class App extends Component {
    state = {  }
    constructor(props){
        super(props);
    }
    render() { 
        return ( 
            <div className="center">
        <HomePage />
        </div>
            );
    }
}
 
export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);