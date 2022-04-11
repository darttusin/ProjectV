import styled from "styled-components";


type contentProps = 'center' | 'left' | 'right' | 'space-between'

interface ButtonFilledStyledProps {
    width: number
    height: number
    justifycontent: contentProps
}

export const ButtonFilledStyled = styled.div`
  width: ${(p: ButtonFilledStyledProps) => p.width}%;
  display: flex;
  justify-content: ${(p: ButtonFilledStyledProps) => p.justifycontent};
  height: ${(p: ButtonFilledStyledProps) => p.height}px;
`