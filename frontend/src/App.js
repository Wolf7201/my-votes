import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomePage from './components/HomePage';
import EventPage from './components/EventPage';
import PollPage from './components/PollPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/event/:code" element={<EventPage/>}/>
                <Route path="/poll/:pollId" element={<PollPage/>}/>
            </Routes>
        </Router>
    );
}

export default App;
