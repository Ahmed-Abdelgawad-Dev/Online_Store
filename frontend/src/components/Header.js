import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";

function Header() {
  return (
    <Navbar variant="dark" bg="gray-800" expand="lg">
      <Container fluid>
        <Navbar.Brand href="/">
          <span className="tw-animate-pulse tw-fw-semibold ">SprintsShop</span>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: "100px" }}
            navbarScroll
          >
            <Nav.Link href="/cart">
              {" "}
              <i className="fas fa-shopping-cart" aria-hidden="true"></i> Cart
            </Nav.Link>
            <Nav.Link href="/login">
              {" "}
              <i className="fas fa-users" aria-hidden="true"></i> Login
            </Nav.Link>
            <Nav.Link href="/products">Products</Nav.Link>
            <Nav.Link href="/about">About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
