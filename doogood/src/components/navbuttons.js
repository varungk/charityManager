import React from 'react';
import cs from './styles/navbts.module.css';

function NavBts(props){
    return(
        <div>
            <li>
                <a className={cs.navbt} href="index.html"><strong>{props.name}</strong></a>
            </li>
        </div>
    )
}

export default NavBts;