import React from "react";
import { Container, Row, Col } from "react-bootstrap";

function Footer() {
  return (
    <>
      <footer>
        <Container>
          <Row>
            <Col className="text-center">copyright &copy; SprinShop</Col>
          </Row>
        </Container>
      </footer>
    </>
  );
}

export default Footer;
