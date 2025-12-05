import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

export const Questionnaire= () => {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    phone_no: "",
    email_address: "",
    address: "",
    postal_code: "",
    dog_type: "",
  });


  // Fetch initial data from /quiz_get
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/quiz_get");
        if (!response.ok) {
          throw new Error("Failed to fetch questionnaire data.");
        }

        const data = await response.json();
        setFormData({
          first_name: data.first_name || "",
          last_name: data.last_name || "",
          phone_no: data.phone_no || "",
          email_address: data.email_address || "",
          address: data.address || "",
          postal_code: data.postal_code || "",
          dog_type: data.dog_type || "",
        });

      } catch (err) {
        console.log(err)
      }
    };

    fetchData();
  }, []);

  // Handle input changes

  // Submit the form data to /quiz_post
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("/quiz_post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Failed to submit questionnaire data.");
      }

      alert("Questionnaire submitted successfully!");
    } catch (err) {
        console.log(err)
    }
  };

  // Display loading or error states

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Adoption Questionnaire</h1>
      <form onSubmit={handleSubmit}>
        {/* First Name */}
        <div className="mb-3">
          <label htmlFor="first_name" className="form-label">
            First Name
          </label>
          <input
            type="text"
            className="form-control"
            id="first_name"
            name="first_name"
            value={formData.first_name}
            required
          />
        </div>

        {/* Last Name */}
        <div className="mb-3">
          <label htmlFor="last_name" className="form-label">
            Last Name
          </label>
          <input
            type="text"
            className="form-control"
            id="last_name"
            name="last_name"
            value={formData.last_name}
            required
          />
        </div>

        {/* Phone Number */}
        <div className="mb-3">
          <label htmlFor="phone_no" className="form-label">
            Phone Number
          </label>
          <input
            type="tel"
            className="form-control"
            id="phone_no"
            name="phone_no"
            value={formData.phone_no}
            required
          />
        </div>

        {/* Email Address */}
        <div className="mb-3">
          <label htmlFor="email_address" className="form-label">
            Email Address
          </label>
          <input
            type="email"
            className="form-control"
            id="email_address"
            name="email_address"
            value={formData.email_address}
            required
          />
        </div>

        {/* Address */}
        <div className="mb-3">
          <label htmlFor="address" className="form-label">
            Address
          </label>
          <input
            type="text"
            className="form-control"
            id="address"
            name="address"
            value={formData.address}
            required
          />
        </div>

        {/* Postal Code */}
        <div className="mb-3">
          <label htmlFor="postal_code" className="form-label">
            Postal Code
          </label>
          <input
            type="text"
            className="form-control"
            id="postal_code"
            name="postal_code"
            value={formData.postal_code}
            required
          />
        </div>

        {/* Dog Type */}
        <div className="mb-3">
          <label htmlFor="dog_type" className="form-label">
            Dog Type
          </label>
          <select
            className="form-select"
            id="dog_type"
            name="dog_type"
            value={formData.dog_type}
            required
          >
            <option value="">Select a Dog Type</option>
            <option value="Labrador">Labrador</option>
            <option value="Golden Retriever">Golden Retriever</option>
            <option value="German Shepherd">German Shepherd</option>
            <option value="Bulldog">Bulldog</option>
            <option value="Poodle">Poodle</option>
            {/* Add more dog types as needed */}
          </select>
        </div>

        {/* Submit Button */}
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  );
};
