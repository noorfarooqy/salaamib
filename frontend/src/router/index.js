import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth.js";

import Login from "@/views/pages/auth/login.vue";
import Register from "@/views/pages/auth/register.vue";
import Forgotpassword from "@/views/pages/auth/forgot-password.vue";
import Lockscreen from "@/views/pages/auth/lockscreen.vue";
import Dashboard from "@/views/pages/dashboard/dashboard.vue";
import AdminDashboard from "@/views/pages/dashboard/index.vue";
import Applications from "@/views/pages/applications/applications.vue";
import Chat from "@/views/pages/applications/chat.vue";
import Email from "@/views/pages/applications/inbox.vue";
import Calendar from "@/views/pages/applications/calendar.vue";
import SuperAdmin from '@/views/pages/superadmin/super-admin.vue'
import Companies from '@/views/pages/superadmin/superadmin-companies.vue'
import Subscription from '@/views/pages/superadmin/superadmin-subscription.vue'
import Packages from '@/views/pages/superadmin/superadmin-packages.vue'
import Domain from '@/views/pages/superadmin/superadmin-domain.vue'
import PurchaseTransaction from '@/views/pages/superadmin/purchase-transaction.vue'
import Customers from "@/views/pages/customers/customers.vue";
import CustomersList from "@/views/pages/customers/customers-list.vue";
import CustomerDetails from "@/views/pages/customers/customer-details.vue";
import Vendors from "@/views/pages/customers/vendors.vue";
import AddCustomer from "@/views/pages/customers/add-customer.vue";
import EditCustomer from "@/views/pages/customers/edit-customer.vue";
import ActiveCustomers from "@/views/pages/customers/active-customers.vue";
import DeactiveCustomers from "@/views/pages/customers/deactive-customers.vue";
import Ledger from "@/views/pages/customers/ledger.vue";
import CustomersLedger from "@/views/pages/customers/customers-ledger.vue";
import ProductService from '@/views/pages/products&services/product-service.vue'
import ProductList from "@/views/pages/products&services/product-list.vue";
import Category from "@/views/pages/products&services/category.vue";
import Units from "@/views/pages/products&services/units.vue";
import AddUnits from "@/views/pages/products&services/add-units.vue";
import Editunits from "@/views/pages/products&services/edit-units.vue";
import AddProducts from "@/views/pages/products&services/add-products.vue";
import EditProducts from "@/views/pages/products&services/edit-products.vue";
import Inventory from "@/views/pages/inventory/inventory.vue";
import AllInventory from "@/views/pages/inventory/all-inventory.vue";
import Signature from '@/views/pages/signature/signature.vue';
import Signaturelist from "@/views/pages/signature/signature-list.vue";
import Signatureinvoice from "@/views/pages/signature/signature-invoice.vue";
import SignaturePreviewInvoice from "@/views/pages/signature/signature-preview-invoice.vue";
import PayOnline from "@/views/pages/signature/pay-online.vue";
import MailPayInvoice from "@/views/pages/signature/mail-pay-invoice.vue";
import InventoryHistory from "@/views/pages/inventory/inventory-history.vue";
import Sales from '@/views/pages/sales/sales.vue';
import Recurringinvoices from "@/views/pages/sales/recurringinvoices/recurring-invoices.vue";
import Recurringpaid from "@/views/pages/sales/recurringinvoices/recurring-paid.vue";
import Recurringpending from "@/views/pages/sales/recurringinvoices/recurring-pending.vue";
import Recurringoverdue from "@/views/pages/sales/recurringinvoices/recurring-overdue.vue";
import Recurringdraft from "@/views/pages/sales/recurringinvoices/recurring-draft.vue";
import Recurring from "@/views/pages/sales/recurringinvoices/recurring.vue";
import Recurringcancelled from "@/views/pages/sales/recurringinvoices/recurring-cancelled.vue";
import CreditNotes from "@/views/pages/sales/creditnotes/credit-notes.vue";
import Addcreditnotes from "@/views/pages/sales/creditnotes/add-credit-notes.vue";
import Editcreditnotes from "@/views/pages/sales/creditnotes/edit-credit-notes.vue";
import Creditnotesdetails from "@/views/pages/sales/creditnotes/credit-notes-details.vue";
import Purchase from '@/views/pages/purchases/purchase.vue'
import PurchasesList from "@/views/pages/purchases/purchases-list.vue";
import Addpurchases from "@/views/pages/purchases/add-purchases.vue";
import Editpurchases from "@/views/pages/purchases/edit-purchases.vue";
import Purchaseorders from "@/views/pages/purchases/purchase-orders.vue";
import Purchasesdetails from "@/views/pages/purchases/purchases-details.vue";
import Debitnotes from "@/views/pages/purchases/debit-notes.vue";
import Invoices from "@/views/pages/sales/invoices/invoices.vue";
import InvoicesList from "@/views/pages/sales/invoices/invoices-list.vue";
import Invoicespaid from "@/views/pages/sales/invoices/invoices-paid.vue";
import Invoicesoverdue from "@/views/pages/sales/invoices/invoices-overdue.vue";
import Invoicesdraft from "@/views/pages/sales/invoices/invoices-draft.vue";
import Invoicesrecurring from "@/views/pages/sales/invoices/invoices-recurring.vue";
import Invoicescancelled from "@/views/pages/sales/invoices/invoices-cancelled.vue";
import Addinvoice from "@/views/pages/sales/invoices/add-invoice.vue";
import Editinvoice from "@/views/pages/sales/invoices/edit-invoice.vue";
import Invoicedetails from "@/views/pages/sales/invoices/invoice-details.vue";
import Invoicesunpaid from "@/views/pages/sales/invoices/invoices-unpaid.vue";
import Invoicesrefunded from "@/views/pages/sales/invoices/invoices-refunded.vue";
import Invoicedetailsadmin from "@/views/pages/sales/invoices/invoice-details-admin.vue";
import Invoicetemplate from "@/views/pages/sales/invoicetemplate/invoice-template.vue";
import Invoice_one_a from "@/views/pages/sales/invoicetemplate/invoice-one-a.vue";
import Invoice_two from "@/views/pages/sales/invoicetemplate/invoice-two.vue";
import Invoice_three from "@/views/pages/sales/invoicetemplate/invoice-three.vue";
import Invoice_four_a from "@/views/pages/sales/invoicetemplate/invoice-four-a.vue";
import Invoice_five from "@/views/pages/sales/invoicetemplate/invoice-five.vue";
import Cashreceipt_1 from "@/views/pages/sales/invoicetemplate/cashreceipt-1.vue";
import Cashreceipt_2 from "@/views/pages/sales/invoicetemplate/cashreceipt-2.vue";
import Cashreceipt_3 from "@/views/pages/sales/invoicetemplate/cashreceipt-3.vue";
import Cashreceipt_4 from "@/views/pages/sales/invoicetemplate/cashreceipt-4.vue";
import Expenses from "@/views/pages/finance/expenses.vue";
import ExpensesList from "@/views/pages/finance/expenses-list.vue";
import Payments from "@/views/pages/finance/payments.vue";
import PaymentsList from "@/views/pages/finance/payments-list.vue";
import Quotations from "@/views/pages/quotations/quotations.vue";
import QuotationsList from "@/views/pages/quotations/quotations-list.vue";
import Editquotations from "@/views/pages/quotations/edit-quotations.vue";
import Addquotations from "@/views/pages/quotations/add-quotations.vue";
import Deliverychallans from "@/views/pages/quotations/delivery-challans.vue";
import Adddeliverychallans from "@/views/pages/quotations/add-delivery-challans.vue";
import Editdeliverychallans from "@/views/pages/quotations/edit-delivery-challans.vue";
import Paymentsummary from "@/views/pages/reports/payment-summary.vue";
import Reports from '@/views/pages/reports/reports/reports.vue'
import Users from "@/views/pages/management/manageuser/users.vue";
import Rolespermission from "@/views/pages/management/roles-permission.vue";
import permission from "@/views/pages/management/permission.vue";
import Deleteaccountrequest from "@/views/pages/management/delete-account-request.vue";
import Membership from '@/views/pages/membership/membership.vue'
import MembershipPlans from "@/views/pages/membership/membership-plans.vue";
import MemberPagesList from "@/views/pages/membership/member-pages-list.vue";
import Membershipaddons from "@/views/pages/membership/membership-addons.vue";
import Subscribers from "@/views/pages/membership/subscribers.vue";
import Transactions from "@/views/pages/membership/transactions.vue";
import Settings from "@/views/pages/settings/settings.vue";
import ProfileSettings from "@/views/pages/settings/profile-settings.vue";
import CompanySettings from "@/views/pages/settings/company-settings.vue";
import InvoiceSettings from "@/views/pages/settings/invoice-settings.vue";
import TemplateInvoice from "@/views/pages/settings/template-invoice/template-invoice.vue";
import PaymentSettings from "@/views/pages/settings/payment-settings.vue";
import BankAccount from "@/views/pages/settings/bank-account.vue";
import TaxRats from '@/views/pages/settings/tax-rats.vue';
import PlanBilling from '@/views/pages/settings/plan-billing.vue';
import TwoFactor from '@/views/pages/settings/two-factor.vue';
import CustomFiled from '@/views/pages/settings/custom-filed.vue';
import EmailSettings from '@/views/pages/settings/email-settings.vue';
import Preferences from '@/views/pages/settings/setting-preferences.vue';
import Email_Template from '@/views/pages/settings/email-template.vue';
import Saas_Settings from '@/views/pages/settings/saas-settings.vue';
import Seo_Settings from '@/views/pages/settings/seo-settings.vue';
import ExpenseReport from '@/views/pages/reports/reports/expense-report.vue'
import PurchaseReport from '@/views/pages/reports/reports/purchase-report.vue'
import PurchaseReturn from '@/views/pages/reports/reports/purchase-return.vue'
import SalesReport from '@/views/pages/reports/reports/sales-report.vue'
import SalesReturnReport from '@/views/pages/reports/reports/sales-return-report.vue'
import QuotationReport from '@/views/pages/reports/reports/quotation-report.vue'
import PaymentReport from '@/views/pages/reports/reports/payment-report.vue'
import StockReport from '@/views/pages/reports/reports/stock-report.vue'
import LowStockReport from '@/views/pages/reports/reports/low-stock-report.vue'
import IncomeReport from '@/views/pages/reports/reports/income-report.vue'
import TaxPurchase from '@/views/pages/reports/reports/tax-purchase.vue'
import Taxsales from '@/views/pages/reports/reports/tax-sales.vue'
import ProfitLossList from '@/views/pages/reports/reports/profit-loss-list.vue'
import Pages from "@/views/pages/content/pages.vue";
import Blogs from '@/views/pages/content/blog/blog.vue'
import AllBlogs from "@/views/pages/content/blog/all-blogs.vue";
import Inactiveblogs from "@/views/pages/content/blog/inactive-blog.vue";
import blogcategories from "@/views/pages/content/blog/categories.vue";
import blogcomments from "@/views/pages/content/blog/blog-comments.vue";
import Locations from '@/views/pages/content/location/locations.vue'
import Countries from "@/views/pages/content/location/countries.vue";
import States from "@/views/pages/content/location/states.vue";
import Cities from "@/views/pages/content/location/cities.vue";
import Testimonials from "@/views/pages/content/testimonials.vue";
import Faq from "@/views/pages/content/faq.vue";
import Contactmessages from "@/views/pages/support/contact-messages.vue";
import Tickets from "@/views/pages/support/ticket/tickets.vue";
import AllTickets from "@/views/pages/support/ticket/all-tickets.vue";
import Ticketslistpending from "@/views/pages/support/ticket/tickets-list-pending.vue";
import Ticketslistoverdue from "@/views/pages/support/ticket/tickets-list-overdue.vue";
import TicketslistResolved from "@/views/pages/support/ticket/tickets-list-resolved.vue";
import TicketslistOpen from "@/views/pages/support/ticket/tickets-list-open.vue";
import TicketslistClosed from "@/views/pages/support/ticket/tickets-list-closed.vue";
import Ticketslist from "@/views/pages/support/ticket/tickets-list.vue";
import Ticketspending from "@/views/pages/support/ticket/tickets-pending.vue";
import Ticketsoverdue from "@/views/pages/support/ticket/tickets-overdue.vue";
import Ticketsdraft from "@/views/pages/support/ticket/tickets-draft.vue";
import Ticketsrecurring from "@/views/pages/support/ticket/tickets-recurring.vue";
import Ticketscancelled from "@/views/pages/support/ticket/tickets-cancelled.vue";
import Ticketdetails from "@/views/pages/support/ticket/ticket-details.vue";
import Ticketkanban from "@/views/pages/support/ticket/tickets-kanban.vue";
import Ticketsopen from "@/views/pages/support/ticket/tickets-open.vue";
import Ticketsresolved from "@/views/pages/support/ticket/tickets-resolved.vue";
import Ticketsclosed from "@/views/pages/support/ticket/tickets-closed.vue";
import Profile from "@/views/pages/pages/profile/profile.vue";
import BlankPage from "@/views/pages/pages/blank-page.vue";
import Error404 from "@/views/pages/pages/error/error-404.vue";
import Baseui from '@/views/pages/uiinterface/baseui/ui-baseui.vue'
import accordions from "@/views/pages/uiinterface/baseui/accordions/ui-accordions.vue";
import alerts from "@/views/pages/uiinterface/baseui/ui-alerts.vue";
import avatar from "@/views/pages/uiinterface/baseui/ui-avatar.vue";
import badges from "@/views/pages/uiinterface/baseui/badges/ui-badges.vue";
import buttongroup from "@/views/pages/uiinterface/baseui/ui-buttongroup.vue";
import buttons from "@/views/pages/uiinterface/baseui/ui-buttons.vue";
import breadcrumbs from "@/views/pages/uiinterface/baseui/ui-breadcrumbs.vue";
import cards from "@/views/pages/uiinterface/baseui/ui-cards.vue";
import carousel from "@/views/pages/uiinterface/baseui/carousel/ui-carousel.vue";
import dropdowns from "@/views/pages/uiinterface/baseui/ui-dropdowns.vue";
import grid from "@/views/pages/uiinterface/baseui/ui-grid.vue";
import images from "@/views/pages/uiinterface/baseui/ui-images.vue";
import lightbox from "@/views/pages/uiinterface/baseui/lightbox/ui-lightbox.vue";
import media from "@/views/pages/uiinterface/baseui/ui-media.vue";
import modal from "@/views/pages/uiinterface/baseui/modal/ui-modal.vue";
import offcanvas from "@/views/pages/uiinterface/baseui/offcanvas/ui-offcanvas.vue";
import pagination from "@/views/pages/uiinterface/baseui/ui-pagination.vue";
import progress from "@/views/pages/uiinterface/baseui/progress/ui-progress.vue";
import placeholders from "@/views/pages/uiinterface/baseui/ui-placeholders.vue";
import spinners from "@/views/pages/uiinterface/baseui/ui-spinners.vue";
import tab from "@/views/pages/uiinterface/baseui/tab/ui-tab.vue";
import toastr from "@/views/pages/uiinterface/baseui/ui-toastr.vue";
import tooltip from "@/views/pages/uiinterface/baseui/ui-tooltip.vue";
import typography from "@/views/pages/uiinterface/baseui/ui-typography.vue";
import video from "@/views/pages/uiinterface/baseui/ui-video.vue";
import Elements from '@/views/pages/uiinterface/elements/ui-elements.vue'
import ribbon from "@/views/pages/uiinterface/elements/ui-ribbon.vue";
import clipboard from "@/views/pages/uiinterface/elements/ui-clipboard.vue";
import dragdrop from "@/views/pages/uiinterface/elements/ui-drag-drop.vue";
import texteditor from "@/views/pages/uiinterface/elements/ui-text-editor.vue";
import counter from "@/views/pages/uiinterface/elements/ui-counter.vue";
import scrollbar from "@/views/pages/uiinterface/elements/ui-scrollbar.vue";
import notificationelement from "@/views/pages/uiinterface/elements/ui-notificationelement.vue";
import timeline from "@/views/pages/uiinterface/elements/ui-timeline.vue";
import horizontaltimeline from "@/views/pages/uiinterface/elements/ui-horizontal-timeline.vue";
import formwizard from "@/views/pages/uiinterface/elements/ui-form-wizard.vue";
import Rating from '@/views/pages/uiinterface/elements/ui-rating.vue'
import Charts from '@/views/pages/uiinterface/chart/ui-charts.vue'
import chartapex from "@/views/pages/uiinterface/chart/apex/chart-apex.vue";
import chartc3 from "@/views/pages/uiinterface/chart/c3/chart-c3.vue";
import chartflot from "@/views/pages/uiinterface/chart/flot/chart-flot.vue";
import chartjs from "@/views/pages/uiinterface/chart/js/chart-js.vue";
import chartmorris from "@/views/pages/uiinterface/chart/morris/chart-morris.vue";
import Icons from '@/views/pages/uiinterface/icons/ui-icons.vue'
import iconfontawesome from "@/views/pages/uiinterface/icons/icon-fontawesome.vue";
import iconfeather from "@/views/pages/uiinterface/icons/icon-feather.vue";
import iconionic from "@/views/pages/uiinterface/icons/icon-ionic.vue";
import iconmaterial from "@/views/pages/uiinterface/icons/icon-material.vue";
import iconpe7 from "@/views/pages/uiinterface/icons/icon-pe7.vue";
import iconsimpleline from "@/views/pages/uiinterface/icons/icon-simpleline.vue";
import iconthemify from "@/views/pages/uiinterface/icons/icon-themify.vue";
import iconweather from "@/views/pages/uiinterface/icons/icon-weather.vue";
import icontypicon from "@/views/pages/uiinterface/icons/icon-typicon.vue";
import iconflag from "@/views/pages/uiinterface/icons/icon-flag.vue";
import Forms from "@/views/pages/uiinterface/form/ui-forms.vue"
import Formbasicinput from "@/views/pages/uiinterface/form/formbasic/form-basic-input.vue";
import Forminput from "@/views/pages/uiinterface/form/forminput/form-input.vue";
import FormHorizontal from "@/views/pages/uiinterface/form/formhorizontal/form-horizontal.vue";
import Formmask from "@/views/pages/uiinterface/form/formmask/form-mask.vue";
import Formselect2 from "@/views/pages/uiinterface/form/form-select2.vue";
import Formfileupload from "@/views/pages/uiinterface/form/form-file-upload.vue";
import Formvalidation from "@/views/pages/uiinterface/form/form-validation.vue";
import Formvertical from "@/views/pages/uiinterface/form/form-vertical.vue";
import Tables from '@/views/pages/uiinterface/table/ui-tables.vue'
import Basictable from "@/views/pages/uiinterface/table/basic-table.vue";
import Datatable from "@/views/pages/uiinterface/table/data-table.vue";
import settingsnotifications from "@/views/pages/settings/notifications.vue";
import ContactDetails from "@/views/pages/content/contact-details.vue";
import Addpurchasesorder from "@/views/pages/purchases/add-purchases-order.vue";
import Addpurchasereturn from "@/views/pages/purchases/add-purchase-return.vue";
import Editpurchasereturn from "@/views/pages/purchases/edit-purchase-return.vue";
import Editpurchasesorder from "@/views/pages/purchases/edit-purchases-order.vue";
import Template_Receipt from "@/views/pages/settings/template-receipt/template-receipt.vue";
import Purchase_Details from "@/views/pages/sales/purchase-details.vue";
import SuperAdminDashboard from '@/views/pages/superadmin/dashboard/superadmin-dashboard.vue'
import DashboardSummary from '@/views/pages/overview/dashboard-summary.vue'
import InvoiceSubscription from '@/views/pages/superadmin/invoice-subscription.vue'
import Plans_List from '@/views/pages/superadmin/plans-list.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta: { requiresGuest: true }
  },
  {
    path: '/payment-summary',
    name: 'payment-summary',
    component: Paymentsummary
  },
  {
    path: '/users',
    name: 'users',
    component: Users
  },
  {
    path: '/roles-permission',
    name: 'roles-permission',
    component: Rolespermission
  },
  {
    path: '/permission',
    name: 'permission',
    component: permission
  },
  {
    path: '/pages',
    name: 'pages',
    component: Pages
  },
  {
    path: '/delete-account-request',
    name: 'delete-account-request',
    component: Deleteaccountrequest
  },
  {
    path: '/testimonials',
    name: 'testimonials',
    component: Testimonials
  },
  {
    path: '/faq',
    name: 'faq',
    component: Faq
  },
  {
    path: '/contact-messages',
    name: 'contact-messages',
    component: Contactmessages
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { requiresGuest: true }
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: Forgotpassword,
    meta: { requiresGuest: true }
  },
  {
    path: '/lock-screen',
    name: 'lock-screen',
    component: Lockscreen,
    meta: { requiresGuest: true }
  },
  {
    path: '/error-404',
    name: 'error-404',
    component: Error404
  },
  {
    path: '/blank-page',
    name: 'blank-page',
    component: BlankPage
  },
  {
    path: '/notifications',
    name: 'notifications',
    component: settingsnotifications
  },
  {
    path: '/contact-details',
    name: 'contact-details',
    component: ContactDetails
  },
  {
    path: '/template-receipt',
    name: 'template-receipt',
    component: Template_Receipt
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true },
    children: [
      { path: "", redirect: "/dashboard/admin-dashboard" },
      { 
        path: "admin-dashboard", 
        component: AdminDashboard,
        meta: { requiresAuth: true }
      },
    ],
  },
  {
    path: '/admin-dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/dashboard/summary',
    name: 'dashboard-summary',
    component: DashboardSummary
  },
  {
    path: "/applications",
    component: Applications,
    children: [
      { path: "", redirect: "/applications/chat" },
      { path: "chat", component: Chat },
      { path: "calendar", component: Calendar },
      { path: "email", component: Email },
    ],
  },
  {
    path: "/super-admin",
    component: SuperAdmin,
    children: [
      { path: "", redirect: "/super-admin/companies" },
      { path: "companies", component: Companies },
      { path: "subscription", component: Subscription },
      { path: "packages", component: Packages },
      { path: "domain", component: Domain },
      { path: "purchase-transaction", component: PurchaseTransaction },
      { path: "dashboard", component: SuperAdminDashboard },
      { path: "invoice-subscription", component: InvoiceSubscription },
      { path: "plans-list", component: Plans_List },
    ],
  },
  {
    path: "/customers",
    component: Customers,
    children: [
      { path: "", redirect: "/customers/customers-list" },
      { path: "customers-list", component: CustomersList },
      { path: "customer-details", component: CustomerDetails },
      { path: "vendors", component: Vendors },
      { path: "ledger", component: Ledger },
      { path: "add-customer", component: AddCustomer },
      { path: "edit-customer", component: EditCustomer },
      { path: "active-customers", component: ActiveCustomers },
      { path: "deactive-customers", component: DeactiveCustomers },
      { path: "customers-ledger", component: CustomersLedger },
    ],
  },
  {
    path: "/product-service",
    component: ProductService,
    children: [
      { path: "", redirect: "/product-service/product-list" },
      { path: "product-list", component: ProductList },
      { path: "category", component: Category },
      { path: "units", component: Units },
      { path: "add-units", component: AddUnits },
      { path: "edit-units", component: Editunits },
      { path: "edit-products", component: EditProducts },
      { path: "add-products", component: AddProducts },
    ],
  },
  {
    path: "/inventory",
    component: Inventory,
    children: [
      { path: "", redirect: "/inventory/all-inventory" },
      { path: "all-inventory", component: AllInventory },
      { path: "inventory-history", component: InventoryHistory }
    ],
  },
  {
    path: "/signature",
    component: Signature,
    children: [
      { path: "", redirect: "/signature/signature-list" },
      { path: "signature-list", component: Signaturelist },
      { path: "signature-invoice", component: Signatureinvoice },
      { path: "signature-preview-invoice", component: SignaturePreviewInvoice },
      { path: "pay-online", component: PayOnline },
      { path: "mail-pay-invoice", component: MailPayInvoice },
    ],
  },
  {
    path: "/sales",
    component: Sales,
    children: [
      { path: "", redirect: "/sales/recurring-invoices" },
      { path: "recurring-invoices", component: Recurringinvoices },
      { path: "recurring-paid", component: Recurringpaid },
      { path: "recurring-pending", component: Recurringpending },
      { path: "recurring-overdue", component: Recurringoverdue },
      { path: "recurring-draft", component: Recurringdraft },
      { path: "recurring", component: Recurring },
      { path: "recurring-cancelled", component: Recurringcancelled },
      { path: "credit-notes", component: CreditNotes },
      { path: "add-credit-notes", component: Addcreditnotes },
      { path: "edit-credit-notes", component: Editcreditnotes },
      { path: "credit-notes-details", component: Creditnotesdetails },
    ],
  },
  {
    path: "/invoices",
    component: Invoices,
    children: [
      { path: "", redirect: "/invoices/invoice-list" },
      { path: "invoice-list", component: InvoicesList },
      { path: "invoices-paid", component: Invoicespaid },
      { path: "invoices-overdue", component: Invoicesoverdue },
      { path: "invoices-draft", component: Invoicesdraft },
      { path: "invoices-recurring", component: Invoicesrecurring },
      { path: "invoices-cancelled", component: Invoicescancelled },
      { path: "edit-invoice", component: Editinvoice },
      { path: "add-invoice", component: Addinvoice },
      { path: "invoice-details", component: Invoicedetails },
      { path: "invoices-unpaid", component: Invoicesunpaid },
      { path: "invoices-refunded", component: Invoicesrefunded },
      { path: "invoice-details-admin", component: Invoicedetailsadmin },
      { path: "invoice-template", component: Invoicetemplate },
      { path: "invoice-one-a", component: Invoice_one_a },
      { path: "invoice-two", component: Invoice_two },
      { path: "invoice-three", component: Invoice_three },
      { path: "invoice-four-a", component: Invoice_four_a },
      { path: "invoice-five", component: Invoice_five },
      { path: "cashreceipt-1", component: Cashreceipt_1 },
      { path: "cashreceipt-2", component: Cashreceipt_2 },
      { path: "cashreceipt-3", component: Cashreceipt_3 },
      { path: "cashreceipt-4", component: Cashreceipt_4 },
    ],
  },
  {
    path: "/purchase",
    component: Purchase,
    children: [
      { path: "", redirect: "/purchase/purchase-list" },
      { path: "purchase-list", component: PurchasesList },
      { path: "add-purchases", component: Addpurchases },
      { path: "edit-purchases", component: Editpurchases },
      { path: "purchase-orders", component: Purchaseorders },
      { path: "purchases-details", component: Purchasesdetails },
      { path: "debit-notes", component: Debitnotes },
      { path: "add-purchases-order", component: Addpurchasesorder },
      { path: "add-purchase-return", component: Addpurchasereturn },
      { path: "edit-purchase-return", component: Editpurchasereturn },
      { path: "edit-purchases-order", component: Editpurchasesorder },
      { path: "purchase-details", component: Purchase_Details },
    ],
  },
  {
    path: "/expenses",
    component: Expenses,
    children: [
      { path: "", redirect: "/expenses/expenses-list" },
      { path: "expenses-list", component: ExpensesList },
    ],
  },
  {
    path: "/payments",
    component: Payments,
    children: [
      { path: "", redirect: "/expenses/payments-list" },
      { path: "payments-list", component: PaymentsList },
    ],
  },
  {
    path: "/quotations",
    component: Quotations,
    children: [
      { path: "", redirect: "/quotations/quotations-list" },
      { path: "quotations-list", component: QuotationsList },
      { path: "edit-quotations", component: Editquotations },
      { path: "add-quotations", component: Addquotations },
      { path: "delivery-challans", component: Deliverychallans },
      { path: "add-delivery-challans", component: Adddeliverychallans },
      { path: "edit-delivery-challans", component: Editdeliverychallans },
    ],
  },
  {
    path: "/reports",
    component: Reports,
    children: [
      { path: "", redirect: "/reports/expense-report" },
      { path: "expense-report", component: ExpenseReport },
      { path: "purchase-report", component: PurchaseReport },
      { path: "purchase-return", component: PurchaseReturn },
      { path: "sales-report", component: SalesReport },
      { path: "sales-return-report", component: SalesReturnReport },
      { path: "quotation-report", component: QuotationReport },
      { path: "payment-report", component: PaymentReport },
      { path: "stock-report", component: StockReport },
      { path: "low-stock-report", component: LowStockReport },
      { path: "income-report", component: IncomeReport },
      { path: "tax-purchase", component: TaxPurchase },
      { path: "profit-loss-list", component: ProfitLossList },
      { path: "tax-sales", component: Taxsales },
    ],
  },
  {
    path: "/membership",
    component: Membership,
    children: [
      { path: "", redirect: "/membership/membership-plans" },
      { path: "membership-plans", component: MembershipPlans },
      { path: "membership-addons", component: Membershipaddons },
      { path: "subscribers", component: Subscribers },
      { path: "transactions", component: Transactions },
      { path: "member-pages-list", component: MemberPagesList },
    ],
  },
  {
    path: "/settings",
    component: Settings,
    children: [
      { path: "", redirect: "/settings/profile-settings" },
      { path: "profile-settings", component: ProfileSettings },
      { path: "company-settings", component: CompanySettings },
      { path: "invoice-settings", component: InvoiceSettings },
      { path: "template-invoice", component: TemplateInvoice },
      { path: "payment-settings", component: PaymentSettings },
      { path: "bank-account", component: BankAccount },
      { path: "tax-rats", component: TaxRats },
      { path: "plan-billing", component: PlanBilling },
      { path: "two-factor", component: TwoFactor },
      { path: "custom-filed", component: CustomFiled },
      { path: "email-settings", component: EmailSettings },
      { path: "preferences", component: Preferences },
      { path: "email-template", component: Email_Template },
      { path: "seo-settings", component: Seo_Settings },
      { path: "saas-settings", component: Saas_Settings },
    ]
  },
  {
    path: "/blogs",
    component: Blogs,
    children: [
      { path: "", redirect: "/blogs/all-blogs" },
      { path: "all-blogs", component: AllBlogs },
      { path: "inactive-blog", component: Inactiveblogs },
      { path: "categories", component: blogcategories },
      { path: "blog-comments", component: blogcomments },
    ]
  },
  {
    path: "/locations",
    component: Locations,
    children : [
      { path: "", redirect: "/locations/countries" },
      { path: "countries", component: Countries },
      { path: "states", component: States },
      { path: "cities", component: Cities },
    ]
  },
  {
    path: "/tickets",
    component: Tickets,
    children : [
      { path: "", redirect: "/tickets/all-tickets" },
      { path: "all-tickets", component: AllTickets },
      { path: "tickets-list-pending", component: Ticketslistpending },
      { path: "tickets-list-overdue", component: Ticketslistoverdue },
      { path: "tickets-list-resolved", component: TicketslistResolved },
      { path: "tickets-list-open", component: TicketslistOpen },
      { path: "tickets-list-closed", component: TicketslistClosed },
      { path: "tickets-list", component: Ticketslist },
      { path: "tickets-pending", component: Ticketspending },
      { path: "tickets-overdue", component: Ticketsoverdue },
      { path: "tickets-draft", component: Ticketsdraft },
      { path: "tickets-recurring", component: Ticketsrecurring },
      { path: "tickets-cancelled", component: Ticketscancelled },
      { path: "ticket-details", component: Ticketdetails },
      { path: "tickets-kanban", component: Ticketkanban },
      { path: "tickets-open", component: Ticketsopen },
      { path: "tickets-resolved", component: Ticketsresolved },
      { path: "tickets-closed", component: Ticketsclosed },
    ]
  },
  {
    path: '/baseui',
    component: Baseui,
    children: [
      { path: '', redirect: '/baseui/accordions' },
      { path: "accordions", component: accordions },
      { path: "alerts", component: alerts },
      { path: "avatar", component: avatar },
      { path: "badges", component: badges },
      { path: "buttongroup", component: buttongroup },
      { path: "buttons", component: buttons },
      { path: "breadcrumbs", component: breadcrumbs },
      { path: "cards", component: cards },
      { path: "carousel", component: carousel },
      { path: "dropdowns", component: dropdowns },
      { path: "grid", component: grid },
      { path: "images", component: images },
      { path: "lightbox", component: lightbox },
      { path: "media", component: media },
      { path: "modals", component: modal },
      { path: "offcanvas", component: offcanvas },
      { path: "pagination", component: pagination },
      { path: "progress", component: progress },
      { path: "placeholders", component: placeholders },
      { path: "spinners", component: spinners },
      { path: "tabs", component: tab },
      { path: "toastr", component: toastr },
      { path: "tooltip", component: tooltip },
      { path: "typography", component: typography },
      { path: "video", component: video },
    ]
  },
  {
    path: '/elements',
    component: Elements,
    children: [
      { path: '', redirect: '/elements/ribbon' },
      { path: "ribbon", component: ribbon },
      { path: "drag-drop", component: dragdrop },
      { path: "rating", component: Rating },
      { path: "clipboard", component: clipboard },
      { path: "text-editor", component: texteditor },
      { path: "counter", component: counter },
      { path: "scrollbar", component: scrollbar },
      { path: "notification", component: notificationelement },
      { path: "timeline", component: timeline },
      { path: "horizontal-timeline", component: horizontaltimeline },
      { path: "form-wizard", component: formwizard },
    ]
  },
  {
    path: '/charts',
    component: Charts,
    children: [
      { path: '', redirect: '/charts/chart-apex' },
      { path: "chart-apex", component: chartapex },
      { path: "chart-c3", component: chartc3 },
      { path: "chart-flot", component: chartflot },
      { path: "chart-js", component: chartjs },
      { path: "chart-morris", component: chartmorris }
    ]
  },
  {
    path: '/icons',
    component: Icons,
    children: [
      { path: '', redirect: '/icons/icon-fontawesome' },
      { path: "icon-fontawesome", component: iconfontawesome },
      { path: "icon-feather", component: iconfeather },
      { path: "icon-ionic", component: iconionic },
      { path: "icon-material", component: iconmaterial },
      { path: "icon-pe7", component: iconpe7 },
      { path: "icon-simpleline", component: iconsimpleline },
      { path: "icon-themify", component: iconthemify },
      { path: "icon-weather", component: iconweather },
      { path: "icon-typicon", component: icontypicon },
      { path: "icon-flag", component: iconflag },
    ]
  },
  {
    path: '/forms',
    component: Forms,
    children: [
      { path: '', redirect: '/forms/form-basic-inputs' },
      { path: "form-basic-inputs", component: Formbasicinput },
      { path: "form-input-groups", component: Forminput },
      { path: "form-horizontal", component: FormHorizontal },
      { path: "form-mask", component: Formmask },
      { path: "form-validation", component: Formvalidation },
      { path: "form-select2", component: Formselect2 },
      { path: "form-fileupload", component: Formfileupload },
      { path: "form-vertical", component: Formvertical },
    ]
  },
  {
    path: '/tables',
    component: Tables,
    children: [
      { path: '', redirect: '/tables/tables-basic' },
      { path: "tables-basic", component: Basictable },
      { path: "data-tables", component: Datatable },
    ]
  },
];

export const router = createRouter({
  history: createWebHistory("/"),
  linkActiveClass: "active",
  routes,
});

router.beforeEach((to, from, next) => {
  // Get auth store instance
  const authStore = useAuthStore()
  
  // Define which routes require authentication
  const requiresAuth = !['/', '/register', '/forgot-password'].includes(to.path)
  
  // Define which routes are for guests only (non-authenticated users)
  const isGuestRoute = ['/', '/register', '/forgot-password'].includes(to.path)
  
  // Check authentication status
  const isAuthenticated = authStore.isAuthenticated

  // Redirect logic
  if (requiresAuth && !isAuthenticated) {
    // If route requires auth and user is not authenticated, redirect to login
    next('/')
  } else if (isGuestRoute && isAuthenticated) {
    // If route is for guests and user is authenticated, redirect to dashboard
    next('/dashboard')
  } else {
    // In all other cases, proceed normally
    next()
  }

  // Scroll to the top of the page
  window.scrollTo({ top: 0, behavior: "smooth" });
  
  // Handle chat page specific body class
  if (to.name === "chat") {
    document.body.classList.add("chat-page");
  } else {
    document.body.classList.remove("chat-page");
  }
});
