import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";

function Header() {
  return (
    <>
      <Navbar bg="gray-900" variant="dark" expand="lg">
        <Container fluid>
          <Navbar.Brand href="/">
            <span className="py-3 rounded-full font-extrabold text-blue-500 transition duration-200 ease-in-out animate-pulse w-6 h-6 skew-y-12">
              SprinShop{" "}
            </span>{" "}
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="me-auto my-lg-0 "
              style={{ maxHeight: "100px" }}
              navbarScroll
            >
              <Nav.Link href="/cart">
                <i class="fa fa-shopping-cart" aria-hidden="true"></i>{" "}
                <span className="font-semibold">Cart</span>
              </Nav.Link>
              <Nav.Link href="/login">
                <i class="fa fa-users" aria-hidden="true"></i>{" "}
                <span className="font-semibold">Login</span>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;
