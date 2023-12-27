import React, {useState} from 'react';
import {useNavigate} from 'react-router-dom';


function HomePage() {
    const [code, setCode] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/anon_users/${code}/get-vote/`);
            const data = await response.json();
            navigate(`/event/${code}`); // Перенаправление на EventPage с id события
        } catch (error) {
            console.error('Ошибка запроса:', error);
        }
    };

    return (
        <div>
            <h1>Введите код доступа</h1>
            <input type="text" value={code} onChange={(e) => setCode(e.target.value)}/>
            <button onClick={handleSubmit}>Отправить</button>
        </div>
    );
}

export default HomePage;