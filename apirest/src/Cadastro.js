import React, {Component} from 'react';
import './App.css';
import api from './api';

class Cadastro extends Component{
  state = {
    livros: [],
  }

  async componentDidMount(){
    const response = await api.post('/livros');

    console.log(response.data);

    this.setState({livros: response.data});
  }

  render(){

    const {livros} = this.state;

    return(
      <div>
        <h1>Livros</h1>
        
      </div>
    )
  }
}

export default Cadastro;