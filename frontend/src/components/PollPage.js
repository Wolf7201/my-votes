import React, {useEffect, useState} from 'react';
import {useParams, useNavigate} from 'react-router-dom';

function PollPage() {
    const {pollId} = useParams();
    const navigate = useNavigate();
    const [pollData, setPollData] = useState(null);
    const [selectedOption, setSelectedOption] = useState(null);

    useEffect(() => {
        const code = localStorage.getItem('voteCode');
        if (!code) {
            console.error('Код голосования не найден');
            return;
        }

        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/anon_users/${code}/get-vote/`);
                const data = await response.json();
                const poll = data.event.polls.find(p => p.id === parseInt(pollId, 10));
                setPollData(poll);
            } catch (error) {
                console.error('Ошибка при получении данных:', error);
            }
        };

        fetchData();
    }, [pollId]);

    const handleSubmit = async () => {
        const code = localStorage.getItem('voteCode');
        if (!code) {
            console.error('Код голосования не найден');
            return;
        }

        try {
            const response = await fetch(`http://localhost:8000/api/anon_users/${code}/add-vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    poll: parseInt(pollId, 10),
                    poll_option: parseInt(selectedOption, 10),
                    anon_user_code: code
                }),
            });

            if (response.ok) {
                alert('Ваш голос учтен!');
                navigate(`/event/${code}`); // Используйте здесь ID события, если оно отличается от code
            } else {
                alert('Произошла ошибка при отправке данных');
            }
        } catch (error) {
            console.error('Ошибка при отправке данных:', error);
            alert('Произошла ошибка при отправке данных');
        }
    };

    if (!pollData) {
        return <div>Загрузка...</div>;
    }

    return (
        <div>
            <h1>Голосование: {pollData.name}</h1>
            <form onSubmit={(e) => e.preventDefault()}>
                {pollData.poll_options.map(option => (
                    <div key={option.id}>
                        <input
                            type="radio"
                            id={`option-${option.id}`}
                            name="pollOption"
                            value={option.id}
                            onChange={(e) => setSelectedOption(e.target.value)}
                        />
                        <label htmlFor={`option-${option.id}`}>{option.value}</label>
                    </div>
                ))}
                <button type="submit" onClick={handleSubmit}>Отправить голос</button>
            </form>
        </div>
    );
}

export default PollPage;
