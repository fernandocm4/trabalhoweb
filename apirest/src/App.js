import React, {Component, useState} from 'react';
import './App.css';
import api from './api';
import Formulario from './Formulario';



class App extends Component{


  state = {
    clientes: [],
  }

  async componentDidMount(){
    const response = await api.get('/infos');

    console.log(response.data);

    this.setState({clientes: response.data});
  }

  render(){

    const {clientes} = this.state;

    return(
      <div className='bloco-central'>
        <div className='bloco1'>
          <h1>Clientes</h1>
          {clientes.map(cliente => (
            <ul key={cliente.id}>{cliente.nome}<br></br>
            {cliente.email}<br></br>
            {cliente.data}</ul>
          ))}
        </div>
        <div className='bloco2'>
          <Formulario></Formulario>
        </div>
      </div>
    )
  }
}

export default App;
