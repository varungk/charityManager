import React from 'react';
import companyLogo from './img/Logo.png';
import './styles/header.css';
import Signup from './signup.js'

function Header(props){
    return(
        <div className="headercontainer">
            <header>
                <div className="heroimage">
                    <img src={companyLogo} alt="BigCo Inc. logo"/>
                </div>
                <Signup name="empty"/>
            </header>
        </div>
    )
}

export default Header;