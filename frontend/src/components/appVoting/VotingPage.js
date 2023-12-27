import React from 'react';
import { useParams } from 'react-router-dom';

function VotingPage({ data }) {
    const { votingId } = useParams();
    if (!data || !Array.isArray(data) || data.length === 0) {
        return <div>Данные о голосованиях отсутствуют или некорректны</div>;
    }
  // Используем useParams для получения параметров маршрута


  // Преобразуем votingId в число
  const votingIdNumber = Number(votingId);

  // Поиск голосования по ID в данных
  const voting = data.find(voting => voting.id === votingIdNumber);

  if (!voting) {
    return <div>Голосование не найдено</div>;
  }

  return (
    <div>
      <h1>{voting.title}</h1>
      <ul>
        {voting.questions.map(question => (
          <li key={question.id}>
            <h2>{question.text}</h2>
            <ul>
              {question.choices.map(choice => (
                <li key={choice.id}>{choice.text}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VotingPage;