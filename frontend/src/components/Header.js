import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import { Link as LinkRouter } from "react-router-dom";
function Header() {
  return (
    <Navbar variant="dark" bg="gray-800" expand="lg">
      <Container fluid>
        <Navbar.Brand>
          <LinkRouter to="/">
            <span className="tw-animate-pulse tw-fw-semibold ">
              SprintsShop
            </span>
          </LinkRouter>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: "100px" }}
            navbarScroll
          >
            <Nav.Link as="div">
              <LinkRouter to="/cart">
                {" "}
                <i className="fas fa-shopping-cart" aria-hidden="true"></i> Cart
              </LinkRouter>
            </Nav.Link>
            <Nav.Link as="div">
              <LinkRouter to="/login">
                {" "}
                <i className="fas fa-users" aria-hidden="true"></i> Login
              </LinkRouter>
            </Nav.Link>
            <Nav.Link as="div">
              <LinkRouter to="/about">About</LinkRouter>
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
