import React, { useState } from 'react';
import api from './api';

const Formulario = () => {

  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [dataNascimento, setDataNascimento] = useState('');

  const handleNomeChange = (event) => {
    setNome(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleDataNascimentoChange = (event) => {
    setDataNascimento(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Aqui você pode realizar alguma ação com os dados do formulário, como enviar para um servidor, etc.
    console.log('Nome:', nome);
    console.log('Email:', email);
    console.log('Data de Nascimento:', dataNascimento);
  };

  return (
    <form onSubmit={handleSubmit}>
        <h1>Cadastro de clientes</h1>
      <div>
        <label htmlFor="nome">Nome:</label>
        <input type="text" id="nome" value={nome} onChange={handleNomeChange} />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" value={email} onChange={handleEmailChange} />
      </div>
      <div>
        <label htmlFor="dataNascimento">Data de Nascimento:</label>
        <input type="date" id="dataNascimento" value={dataNascimento} onChange={handleDataNascimentoChange} />
      </div>
      <button type="submit">Enviar</button>
    </form>
  );
};

export default Formulario;
