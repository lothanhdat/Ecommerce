import React from "react";
import { Nav } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

function CheckoutSteps({ step1, step2, step3, step4 }) {
  return (
    <Nav className="content-center mb-4">
      <Nav.Item>
        {step1 ? (
          <LinkContainer to="/login">
            <Nav.Link>
              <h2>LOGIN</h2>
            </Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>
            <h2>LOGIN</h2>
          </Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step2 ? (
          <LinkContainer to="/shipping">
            <Nav.Link>
              <h2>SHIPPING</h2>
            </Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>
            <h2>SHIPPING</h2>
          </Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step3 ? (
          <LinkContainer to="/payment">
            <Nav.Link>
              <h2>PAYMENT</h2>
            </Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>
            <h2>PAYMENT</h2>
          </Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step4 ? (
          <LinkContainer to="/placeorder">
            <Nav.Link>
              <h2>PLACE ORDER</h2>
            </Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>
            <h2>PLACE ORDER</h2>
          </Nav.Link>
        )}
      </Nav.Item>
    </Nav>
  );
}

export default CheckoutSteps;
