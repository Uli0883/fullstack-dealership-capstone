import React, { useState } from 'react';

function Register() {
    const [form, setForm] = useState({
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Register data:', form);
        alert('User registered!');
    };

    return (
        <div className="container mt-5">
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Username</label>
                    <input type="text" name="username" className="form-control" value={form.username} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>First Name</label>
                    <input type="text" name="first_name" className="form-control" value={form.first_name} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>Last Name</label>
                    <input type="text" name="last_name" className="form-control" value={form.last_name} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>Email</label>
                    <input type="email" name="email" className="form-control" value={form.email} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" name="password" className="form-control" value={form.password} onChange={handleChange} required />
                </div>
                <button type="submit" className="btn btn-success">Register</button>
            </form>
        </div>
    );
}

export default Register;