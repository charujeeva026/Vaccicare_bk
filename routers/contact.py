# from fastapi import APIRouter, Request, status
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, EmailStr
# from utils_email import send_email

# router = APIRouter(
#     prefix="/contact",
#     tags=["Contact"]
# )

# class ContactForm(BaseModel):
#     name: str
#     email: EmailStr
#     message: str

# @router.post("/send", status_code=status.HTTP_200_OK)
# async def send_contact_email(form: ContactForm):
#     subject = f"New Contact Form Message from {form.name}"
#     body = f"""
#     <h2>Contact Form Message</h2>
#     <p><strong>Name:</strong> {form.name}</p>
#     <p><strong>Email:</strong> {form.email}</p>
#     <p><strong>Message:</strong></p>
#     <p>{form.message}</p>
#     """
#     try:
#         # replace this with admin/support email
#         recipients = ["support@vaccicare.com"]  
#         await send_email(subject, recipients, body)
#         return {"message": "Your message has been sent successfully!"}
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"message": f"Failed to send message: {e}"}
#         )