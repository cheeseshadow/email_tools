from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment and specify the directory of your templates
env = Environment(loader=FileSystemLoader('.'))

# Load the template by name
template = env.get_template('template.html')

# Create a context for the template to render with
context = {
    'swappie_care_trial': 'Your Swappie Care trial ends in 7 days',
    'hello_customer': 'Hi {{ customer.first_name }},',
    'trial_ends_soon': 'We just wanted to let you know that your trial for Swappie Care ends soon and the first payment is due in <b>7 days</b>. We’re thrilled to have you on board!',
    'first_payment_on': 'First payment on: {{ subscription.next_billing_at | format: dd-MM-yyyy}}',
    'subscription_fee': 'Subscription fee: {{ plan.price }}',
    'your_order_number': 'Your order number: {{ subscription.po_number }}',
    'manage_your_subscription': '<a href="https://swappie.com/en/myswappie/">Manage your subscription</a>',
    'if_you_have_any_questions': 'Please let us know if you have any questions by <a href="https://help.swappie.com/en/contact/submit-a-request-SJCaBh8P">messaging us</a>.',
    'kind_regards': 'Kind regards,',
}

# Render the template with the context
rendered_template = template.render(context)

# Print the rendered template (or write it to a file)
with open('temp.html', 'w') as f:
    f.write(rendered_template)

