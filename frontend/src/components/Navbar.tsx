//Nav Bar so the user can navigate between the pages
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import "../styles/Navbar.css";

import { NavBarButtons } from './navbarbutton';
// import React, { useState } from "react";
// import { useAuth0 } from "@auth0/auth0-react";


const Navbar_pet = () => {


  return (
    <>
    <Navbar bg="light" data-bs-theme="light" className="navbar-top">
        <Container className='container'>
          <Navbar.Brand href="#" className="navbar-brand">FindAPet.com</Navbar.Brand>
          <Nav>
            <NavBarButtons/>
          </Nav>  
      </Container>
    </Navbar>
    <br />
    <Navbar bg="light" data-bs-theme="light" className='navbar-bottom'>
        <Container>
          <Nav>
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/about">About</Nav.Link>
            <Nav.Link as={Link} to="/pet_quiz">Pet Quiz</Nav.Link>
            <Nav.Link as={Link} to="/shop">Shop</Nav.Link>
            <Nav.Link as={Link} to="/settings">Settings</Nav.Link>
          </Nav>
      </Container>
      </Navbar>
      <br />
    </>
  );
}

export default Navbar_pet;
