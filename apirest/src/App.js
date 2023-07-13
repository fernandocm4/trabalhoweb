import React, {Component, useState} from 'react';
import './App.css';
import api from './api';


class App extends Component{


  state = {
    livros: [],
  }

  async componentDidMount(){
    const response = await api.get('/livros');

    console.log(response.data);

    this.setState({livros: response.data});
  }

  render(){

    const {livros} = this.state;

    return(
      <div className='bloco-central'>
        <div className='bloco1'>
          <h1>Livros</h1>
          {livros.map(livro => (
            <li key={livro.id}>{livro.título}</li>
          ))}
        </div>
        <div className='bloco2'>
          <form action="App.js" method="POST">
            <h1>Cadastro</h1>
            <label>Título do livro</label>
            <input type="text" name="titulo"/>
            <label>Autor do livro</label>
            <input type="text" name="autor" />
            <input type="submit" value="Enviar" />
          </form>
        </div>
      </div>
    )
  }
}

export default App;
