import React from 'react';
import navcss from './styles/navbutton.module.css';
import NavBts from './navbuttons.js'

function Searchbar(props){
    return(
        <div className={navcss.navcontainer}>
            <div className={navcss.wrapper}>
                <nav>
                    <div className={navcss.logo}>
                        doogood
                    </div>
                    <ul className={navcss.navitems}>
                        <NavBts  name={"Home"}/>
                        <NavBts  name={"Browse"}/>
                        <NavBts  name={"Blog"}/>
                    </ul>
                </nav>
            </div>
        </div>
    )
}

export default Searchbar;