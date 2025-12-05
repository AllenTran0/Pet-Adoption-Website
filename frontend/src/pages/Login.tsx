import { useState } from 'react';
import Container from 'react-bootstrap/Container';
import { useAuth0 } from "@auth0/auth0-react";


const Login = () => {
    const [username, setUser] = useState('');
    const [password, setPassword] = useState('');

    const onButtonClick = () => {
    
    };
    return(
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={onButtonClick}/>
            <Container>
                <label htmlFor="username"><b>Username</b></label>
                <input 
                    type="usernname" 
                    placeholder='Enter Username' 
                    value={username}
                    onChange={(e) => setUser(e.target.value)} 
                    required
                />
                <label htmlFor="password"><b>Password</b></label>
                <input 
                    type="password" 
                    placeholder='Enter Password' 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)} 
                    required
                />

                <button type="submit">Login</button>
            </Container>
        </div>

    

    );

}

export default Login;
