import React, { Component } from 'react';
import axios from 'axios';


class VotingList extends Component {
  state = {
    votings: []
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/voting/')
      .then(res => {
        const votings = res.data;
        this.setState({ votings });
        //!!!!для отладки, перед продом удалить
        console.log(res.data)
        ///!!!!для отладки, перед продом удалить
      })
  }

  render() {
    return (
      <ul>
        {this.state.votings.map(voting =>
          <li key={voting.id}><a href={`voting/${voting.id}`}>{voting.title}</a> <p> Код приглашения {voting.invitation_code}</p></li>
        )}
      </ul>
    )
  }
}

export default VotingList;