import React, { Component } from 'react';
import VotingList from '../appVoting/VotingList';
import Header from '../appHeader/Header';
import Footer from '../appFooter/Footer';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import VotingPage from '../appVoting/VotingPage';
import axios from 'axios'; // Импортируйте axios

class App extends Component {
  state = {
    votings: [], // Инициализируйте состояние для данных о голосованиях
  }

  componentDidMount() {
    // Загрузите данные о голосованиях в этом методе
    axios.get('http://127.0.0.1:8000/api/voting/')
      .then(res => {
        const votings = res.data;
        this.setState({ votings });
      })
  }

  render() {
    return (
    <div>
      <Header />
      <Router>
        <Routes>
          <Route path="/" element={<VotingList data={this.state.votings} />} />
          <Route path="/voting/:votingId" element={<VotingPage data={this.state.votings} />} />
        </Routes>
      </Router>
      <Footer />
    </div>
    );
  }
}

export default App;