import styled from "styled-components";
import {Typography, TypographyProps} from "antd";

const {Text} = Typography

type fontWeightType = 'normal' | 'bold' | 'bolder' | 'lighter'

interface TextStyledProps {
    color: string
    textSize: number
    fontWeight: fontWeightType
}

export const TextStyled = styled(Text)`
  color: ${(p: TextStyledProps) => p.color};
  font-size: ${(p: TextStyledProps) => p.textSize}px;
  font-weight: ${(p: TextStyledProps) => p.fontWeight};
`