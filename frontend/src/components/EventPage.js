// EventPage.js
import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function EventPage() {
    const { code } = useParams();
    const navigate = useNavigate();
    const [eventData, setEventData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/anon_users/${code}/get-vote/`);
                const data = await response.json();
                setEventData(data.event);
            } catch (error) {
                console.error('Ошибка при получении данных:', error);
            }
        };

        fetchData();
    }, [code]);

    const handlePollClick = (pollId) => {
        navigate(`/poll/${pollId}`); // Переход на страницу голосования
    };

    if (!eventData) {
        return <div>Загрузка...</div>;
    }

    return (
        <div>
            <h1>Событие: {eventData.name}</h1>
            <h2>Статус: {eventData.status}</h2>
            <div>
                <h3>Голосования:</h3>
                {eventData.polls.map(poll => (
                    <div key={poll.id}>
                        <h4>{poll.name}</h4>
                        <p>Статус: {poll.status}</p>
                        <button onClick={() => handlePollClick(poll.id)}>Перейти</button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default EventPage;
