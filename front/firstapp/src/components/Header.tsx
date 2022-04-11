import React from 'react';
import '../App.css';
import {HeaderStyled} from "../styledComponent/Header-styled";
import {TextStyled} from '../styledComponent/TextStyled';
import {useHistory} from "react-router-dom";


const HeaderComponent: React.FC = () => {
    const history = useHistory()

    const upload = () => {
        history.push('/upload')
    }

    return (
        <HeaderStyled>
            <TextStyled textSize={25} color={'white'} fontWeight={'normal'}>
                ProjectV
            </TextStyled>
        </HeaderStyled>
    )
}


export default HeaderComponent;