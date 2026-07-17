import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import EligibilityForm from './EligibilityForm';

test('renders eligibility form', () => {
  render(<EligibilityForm />);
  expect(screen.getByText(/Check Your Eligibility/i)).toBeInTheDocument();
});
