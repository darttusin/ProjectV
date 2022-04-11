import React from 'react';
import '../App.css';
import { FooterStyled } from '../styledComponent/Footer-styled';
import { TextStyled } from '../styledComponent/TextStyled';



const FooterComponent: React.FC = () => (
    <FooterStyled>
        <TextStyled textSize={20} color={'white'} fontWeight={'normal'}>
            ®All rights reserved
        </TextStyled>
        <TextStyled textSize={20} color={'white'} fontWeight={'normal'}>
            by FastTeam
        </TextStyled>
    </FooterStyled>
)


export default FooterComponent;