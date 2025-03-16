import { createApp } from 'vue';
import { createPinia } from 'pinia'
import { router } from '@/router';
import App from "@/App.vue";
import {BootstrapVue3, BToastPlugin} from 'bootstrap-vue-3'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';
import FlagIcon from 'vue-flag-icon';
import VueSelect from 'vue3-select2-component'
import DatePicker from 'vue3-datepicker'
import Vue3Autocounter from 'vue3-autocounter';
import Toaster from '@meforma/vue-toaster'
import VueSweetalert2 from 'vue-sweetalert2' 
import 'sweetalert2/dist/sweetalert2.min.css';
import StarRating from 'vue-star-rating'
import VueFeather from 'vue-feather';
import VueApexCharts from "vue3-apexcharts"; 
import VueEasyLightbox from "vue-easy-lightbox";
import "vue-cool-lightbox/dist/vue-cool-lightbox.min.css";
import VueFormWizard from "vue3-form-wizard";
import VueTelInput from 'vue3-tel-input'
import 'vue3-tel-input/dist/vue3-tel-input.css'
import { useAuthStore } from './stores/auth';
import Themifyicon from "vue-themify-icons";
import SimpleLineIcons from "vue-simple-line";

/*********Header component**********/
import MainHeader from '@/views/layouts/layout-header.vue'
import Invoicefilter from '@/views/layouts/invoice-filter.vue'

/*********Sidebar component**********/
import MainSidebar from '@/views/layouts/layout-sidebar.vue'
import Navbar from '@/views/layouts/navbar-nav.vue'
import SidebarItems from '@/views/layouts/sidebar-items.vue'

/*********Pageheader component**********/
import breadcrumb from '@/components/breadcrumb/breadcrumb.vue'
import pageheader from '@/components/breadcrumb/page-header.vue'
import pageticketheader from '@/components/breadcrumb/pageticket-header.vue'
import Ticketheader from '@/components/breadcrumb/ticket-header.vue'
import Supportheader from '@/components/breadcrumb/support-header.vue'
import blogheader from '@/components/breadcrumb/blog-header.vue'
import Allblogheader from '@/components/breadcrumb/allblog-header.vue'
import Inactiveblogheader from '@/components/breadcrumb/inactiveblog-header.vue'
import locationheader from '@/components/breadcrumb/location-header.vue'
import InventoryHeader from '@/components/breadcrumb/inventory-header.vue'
import Blogcommentsheader from '@/components/breadcrumb/blogcomments-header.vue'
import Recurringheader from '@/components/breadcrumb/recurring-header.vue'
import Userheader from '@/components/breadcrumb/user-header.vue'
import Purchasesheader from '@/components/breadcrumb/purchases-header.vue'
import Paymentheader from '@/components/breadcrumb/payment-header.vue'
import Quotationsheader from '@/components/breadcrumb/quotations-header.vue'
import Debitnotesheader from '@/components/breadcrumb/debitnotes-header.vue'
import ProductListHeader from '@/components/breadcrumb/productlist-header.vue'
import CategoryHeader from '@/components/breadcrumb/category-header.vue'
import UnitsHeader from '@/components/breadcrumb/units-header.vue'
import CustomerHeader from '@/components/breadcrumb/customer-header.vue'
import DeactiveCustomerHeader from '@/components/breadcrumb/deactivecustomer-header.vue'
import VendorsHeader from '@/components/breadcrumb/vendors-header.vue'
import Testimonialsheader from '@/components/breadcrumb/testimonials-header.vue'
import Countriesheader from '@/components/breadcrumb/countries-header.vue'
import Stateheader from '@/components/breadcrumb/state-header.vue'
import Citiesheader from '@/components/breadcrumb/cities-header.vue'
import Invoiceheader from '@/components/breadcrumb/invoice-header.vue'
import SuperAdminHeader from '@/components/breadcrumb/superadmin-header.vue'
import Packageheader from '@/components/breadcrumb/package-header.vue'
import InventoryHistoryHeader from '@/components/breadcrumb/inventory-historyheader.vue'
import InvoicesHeader from '@/components/breadcrumb/invioces-header.vue'
import Permissionheader from '@/components/breadcrumb/permission-header.vue'
import Membershiplanheader from '@/components/breadcrumb/membershiplan-header.vue'
import Membershipheader from '@/components/breadcrumb/membership-header.vue'
import Reportheader from '@/components/breadcrumb/report-header.vue'
import Ledgerheader from '@/components/breadcrumb/ledger-header.vue'
import CompaniesHeader from '@/components/breadcrumb/companies-header.vue'
import SubscriptionHeader from '@/components/breadcrumb/subscription-header.vue'
import PackagesHeader from '@/components/breadcrumb/packages-header.vue'
import DomainHeader from '@/components/breadcrumb/domain-header.vue'

/************Page Components********************/
import Inputsize from '@/views/pages/uiinterface/form/formbasic/input-size.vue'
import Addressform from '@/views/pages/uiinterface/form/formhorizontal/address-form.vue'
import Basicform from '@/views/pages/uiinterface/form/formhorizontal/basic-form.vue'
import Personaldetail from '@/views/pages/uiinterface/form/formhorizontal/personal-detail.vue'
import Personalinformation from '@/views/pages/uiinterface/form/formhorizontal/personal-information.vue'
import Contexttable from '@/views/pages/uiinterface/table/context-table.vue'
import Settingsidebar from '@/views/pages/settings/setting-sidebar'
import searchfilter from '@/views/pages/support/ticket/search-filter'
import Ticketcard from '@/views/pages/support/ticket/ticket-card'
import Tickettab from '@/views/pages/support/ticket/ticket-tab'
import Ticketstabs from '@/views/pages/support/ticket/tickets-tabs'
import BlogList from '@/views/pages/content/blog/blog-list.vue'
import Invoicecard from '@/views/pages/sales/invoice-card'
import Invoicetab from '@/views/pages/sales/invoices-tab'
import RecurringInvoicecard from '@/views/pages/sales/recurringinvoices/invoice-card'
import RecurringInvoicetab from '@/views/pages/sales/recurringinvoices/invoice-tab'
import Credittab from '@/views/pages/sales/creditnotes/credit-tab'
import Signatureedit from '@/views/pages/signature/signature-edit'
import SignatureTable from '@/views/pages/signature/signature-table'
import SelectBank from '@/views/pages/signature/select-bank'
import Invoice from '@/views/pages/settings/template-invoice/invoice'
import Purchase from '@/views/pages/settings/template-invoice/template-invoice-purchase'
import Receipt from '@/views/pages/settings/template-invoice/template-invoice-receipt'
import Template_Invoice_Tabs from '@/views/pages/settings/template-invoice/template-invoice-tabs'
import Receipt_Invoice from '@/views/pages/settings/template-receipt/receipt-invoice'
import LightBoxOne from '@/views/pages/uiinterface/baseui/lightbox/lightbox-one.vue'
import LightBoxTwo from '@/views/pages/uiinterface/baseui/lightbox/lightbox-two.vue'
import Bordered from '@/views/pages/uiinterface/baseui/accordions/accord-bordered.vue'
import BorderedJustified from '@/views/pages/uiinterface/baseui/accordions/accord-borderedjustified.vue'
import Default from '@/views/pages/uiinterface/baseui/accordions/accord-default.vue'
import Justified from '@/views/pages/uiinterface/baseui/accordions/accord-justified.vue'
import Questions from '@/views/pages/uiinterface/baseui/accordions/accord-questions.vue'
import Vakal from '@/views/pages/uiinterface/baseui/accordions/accord-vakal.vue'
import Verticalleft from '@/views/pages/uiinterface/baseui/accordions/accord-verticalleft.vue'
import VerticalRight from '@/views/pages/uiinterface/baseui/accordions/accord-verticalright.vue'
import Gradientbadges from '@/views/pages/uiinterface/baseui/badges/gradient-badges.vue'
import BadgesOne from '@/views/pages/uiinterface/baseui/badges/badges-one.vue'
import Pillbadges from '@/views/pages/uiinterface/baseui/badges/pill-badges.vue'
import Carouselthree from '@/views/pages/uiinterface/baseui/carousel/carousel-three.vue'
import Carouseltwo from '@/views/pages/uiinterface/baseui/carousel/carousel-two.vue'
import Carouselone from '@/views/pages/uiinterface/baseui/carousel/carousel-one.vue'
import Bootstrapmodal from '@/views/pages/uiinterface/baseui/modal/bootstrap-modal.vue'
import Custommodal from '@/views/pages/uiinterface/baseui/modal/custom-modal.vue'
import Modelalert from '@/views/pages/uiinterface/baseui/modal/modal-alert.vue'
import Multiplemodal from '@/views/pages/uiinterface/baseui/modal/multiple-modal.vue'
import Pagemodals from '@/views/pages/uiinterface/baseui/modal/page-modals.vue'
import Positionmodal from '@/views/pages/uiinterface/baseui/modal/position-modal.vue'
import Staticmodal from '@/views/pages/uiinterface/baseui/modal/static-modal.vue'
import Backdrop from '@/views/pages/uiinterface/baseui/offcanvas/offcanvas-backdrop.vue'
import Offcanvasone from '@/views/pages/uiinterface/baseui/offcanvas/offcanvas-one.vue'
import Placement from '@/views/pages/uiinterface/baseui/offcanvas/offcanvas-placement.vue'
import Largeprogress from '@/views/pages/uiinterface/baseui/progress/large-progress.vue'
import Defaultprogress from '@/views/pages/uiinterface/baseui/progress/default-progress.vue'
import Mediumprogress from '@/views/pages/uiinterface/baseui/progress/medium-progress.vue'
import Smallprogress from '@/views/pages/uiinterface/baseui/progress/small-progress.vue'
import Extrasmallprogress from '@/views/pages/uiinterface/baseui/progress/extrasmall-progress.vue'
import Basictab from '@/views/pages/uiinterface/baseui/tab/basic-tab.vue'
import Bottomtab from '@/views/pages/uiinterface/baseui/tab/bottom-tab.vue'
import Linetab from '@/views/pages/uiinterface/baseui/tab/line-tab.vue'
import Roundtab from '@/views/pages/uiinterface/baseui/tab/round-tab.vue'
import Solidtab from '@/views/pages/uiinterface/baseui/tab/solid-tab.vue'
import SideSettings from '@/views/layouts/side-settings.vue'
import Userfilter from '@/views/pages/management/manageuser/user-filter.vue'



/************profile page *********/
import ProfileTable from '@/views/pages/pages/profile/ProfileTable.vue'
import ProfileTable1 from '@/views/pages/pages/profile/ProfileTable1.vue'
import ProfileContent from '@/views/pages/pages/profile/ProfileContent.vue'
/*********Dashboard**********/
import DashboardPage from '@/views/pages/dashboard/index-page.vue'


/*********Modal component**********/
import Ticketmodal from '@/components/modal/ticket-modal.vue'
import Locationmodal from '@/components/modal/location-modal.vue'
import InventoryModel from '@/components/modal/inventory-model.vue'
import SignatureModel from '@/components/modal/signature-model.vue'
import Companies_Model from '@/components/modal/companies-model.vue'
import Subscription_Model from '@/components/modal/subscription-model.vue'
import DeleteModal from '@/components/modal/delete-modal.vue'
import CustomersLedgerModal from '@/components/modal/customers-ledger-modal.vue'
import Quotationreportmodal from '@/components/modal/quotationreport-modal.vue'
import Quotationmodel from '@/components/modal/quotation-model.vue'
import Purchasemodel from '@/components/modal/purchase-model.vue'
import Purchasereturnmodel from '@/components/modal/purchasereturn-model.vue'
import Expensemodel from '@/components/modal/expense-model.vue'
import Salesmodel from '@/components/modal/sales-model.vue'
import Salesreturnmodel from '@/components/modal/salesreturn-model.vue'
import Paymentmodel from '@/components/modal/payment-model.vue'
import Stockmodel from '@/components/modal/stock-model.vue'
import Lowstockmodel from '@/components/modal/lowstock-model.vue'
import Incomemodel from '@/components/modal/income-model.vue'
import Taxpurchasemodel from '@/components/modal/taxpurchase-model.vue'
import Profitmodel from '@/components/modal/profit-model.vue'
import Taxratsmodel from '@/components/modal/taxrats-model.vue'
import Customfiledmodel from '@/components/modal/customfiled-model.vue'
import Usermodel from '@/components/modal/user-model.vue'
import Deleteaccountrequestmodel from '@/components/modal/deleteaccountrequest-model.vue'
import Membershiplanmodel from '@/components/modal/membershiplan-model.vue'
import Subscribersmodel from '@/components/modal/subscribers-model.vue'
import Pagemodel from '@/components/modal/page-model.vue'
import Faqmodel from '@/components/modal/faq-model.vue'
import Testimonialsmodel from '@/components/modal/testimonials-model.vue'
import Allblogmodel from '@/components/modal/allblog-model.vue'
import Categoriesmodel from '@/components/modal/categories-model.vue'
import Inactiveblogmodel from '@/components/modal/inactiveblog-model.vue'
import Countriesmodel from '@/components/modal/countries-model.vue'
import Statesmodel from '@/components/modal/states-model.vue'
import Citiesmodel from '@/components/modal/cities-model.vue'
import ExpensesModal from '@/components/modal/expenses-modal.vue'
import Ticketkanbanmodel from '@/components/modal/ticketkanban-model.vue'
import Contactdetailsmodel from '@/components/modal/contactdetails-model.vue'
import Ledgermodal from '@/components/modal/ledger-modal.vue'
import Packages_Modal from '@/components/modal/packages-modal.vue'
import Seo_Settings_Modal from '@/components/modal/seo-settings-modal.vue'
import Saas_Settings_Modal from '@/components/modal/saas-settings-modal.vue'
import Email_Template_Modal from '@/components/modal/email-template-modal.vue'
import Domain_Modal from '@/components/modal/domain-modal.vue'



import ElementBreadcrumb from '@/components/breadcrumb/element-breadcrumb.vue'
import Taxpurchaseheader from '@/components/breadcrumb/taxpurchase-header.vue'
import Profitlosslistheader from '@/components/breadcrumb/profitlosslist-header.vue'


/************************ Header   ****************/
import Quotationreportheader from '@/components/breadcrumb/quotationreport-header.vue'
import Paymentreportheader from '@/components/breadcrumb/paymentreport-header.vue'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '@fortawesome/fontawesome-free/css/fontawesome.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'material-icons/css/material-icons.min.css';
import 'material-icons/css/material-icons.css';
import 'pe7-icon/dist/dist/pe-icon-7-stroke.css';
import 'typicons.font/src/font/typicons.css';
import 'weathericons/css/weather-icons.css'
import 'ionicons-npm/css/ionicons.css';
import '@/assets/css/vue-form-wizard.css';
import '@/assets/css/feather.css';
import '@/assets/css/style.css'; 



import swal from 'sweetalert2';

window.Swal = swal;
const app = createApp(App)

// Initialize Pinia first
const pinia = createPinia()
app.use(pinia)

// Now we can safely use stores
const authStore = useAuthStore()
authStore.initialize()

/*********Header component**********/
app.component('layout-header', MainHeader)
app.component('invoicefilter', Invoicefilter);
/*********Sidebar component**********/
app.component('layout-sidebar', MainSidebar)
app.component('navbar', Navbar)
app.component('sidebar-items', SidebarItems)

/*********Pageheader component**********/
app.component('breadcrumb', breadcrumb)
app.component('pageheader', pageheader)
app.component('ticketheader', pageticketheader)
app.component('ticketlistheader', Ticketheader)
app.component('invoiceheader', Invoiceheader)
app.component('userheader', Userheader)
app.component('recurringheader', Recurringheader)
app.component('blogcommentsheader', Blogcommentsheader)
app.component('quotationsheader', Quotationsheader)
app.component('debitnotesheader', Debitnotesheader)
app.component('purchasesheader', Purchasesheader)
app.component('supportheader', Supportheader)
app.component('paymentheader', Paymentheader)
app.component('blogheader', blogheader)
app.component('allblogheader', Allblogheader)
app.component('inactiveblogheader', Inactiveblogheader)
app.component('locationheader', locationheader)
app.component('inventoryheader',InventoryHeader)
app.component('productlistheader',ProductListHeader)
app.component('categoryheader',CategoryHeader)
app.component('unitsheader',UnitsHeader)
app.component('customerheader',CustomerHeader)
app.component('deactivecustomerheader',DeactiveCustomerHeader)
app.component('vendorsheader',VendorsHeader)
app.component('testimonialsheader',Testimonialsheader)
app.component('countriesheader',Countriesheader)
app.component('stateheader',Stateheader)
app.component('citiesheader',Citiesheader)
app.component('receipt-invoice',Receipt_Invoice)
app.component('superadminheader', SuperAdminHeader)
app.component('packageheader', Packageheader)
app.component('inventory-historyheader', InventoryHistoryHeader)
app.component('invoices-header', InvoicesHeader)
app.component('permissionheader',Permissionheader)
app.component('membershiplanheader',Membershiplanheader)
app.component('membershipheader',Membershipheader)
app.component('reportheader',Reportheader)
app.component('ledgerheader',Ledgerheader)
app.component('companies-header', CompaniesHeader)
app.component('subscription-header', SubscriptionHeader)
app.component('packages-header', PackagesHeader)
app.component('domain-header', DomainHeader)

/************Page Components********************/
app.component('inputsize', Inputsize);
app.component('personaldetail', Personaldetail);
app.component('personalinformation', Personalinformation);
app.component('addressform', Addressform);
app.component('basicform', Basicform);
app.component('contexttable', Contexttable);
app.component('settingsidebar', Settingsidebar);
app.component('searchfilter', searchfilter);
app.component('card', Ticketcard);
app.component('tab', Tickettab);
app.component('tickettab', Ticketstabs);
app.component('blog-list', BlogList);
app.component('invoicecard', Invoicecard);
app.component('invoice-card', RecurringInvoicecard);
app.component('invoice-tab', RecurringInvoicetab);
app.component('credit-tab', Credittab);
app.component('invoicetab', Invoicetab)
app.component('lightboxone',LightBoxOne)
app.component('lightboxtwo',LightBoxTwo)
app.component('bordered',Bordered)
app.component('borderedjustified',BorderedJustified)
app.component('default',Default)
app.component('justified',Justified)
app.component('questions',Questions)
app.component('vakal',Vakal)
app.component('verticalleft',Verticalleft)
app.component('verticalright',VerticalRight)
app.component('gradientbadges',Gradientbadges)
app.component('badgesone',BadgesOne)
app.component('pillbadges',Pillbadges)
app.component('carouselone',Carouselone)
app.component('carouseltwo',Carouseltwo)
app.component('carouselthree',Carouselthree)
app.component('bootstrapmodal',Bootstrapmodal)
app.component('custommodal',Custommodal)
app.component('modalalert',Modelalert)
app.component('multiplemodal',Multiplemodal)
app.component('pagemodals',Pagemodals)
app.component('positionmodal',Positionmodal)
app.component('staticmodal',Staticmodal)
app.component('backdrop',Backdrop)
app.component('placement',Placement)
app.component('offcanvasone',Offcanvasone)
app.component('smallprogress',Smallprogress)
app.component('extrasmallprogress',Extrasmallprogress)
app.component('mediumprogress',Mediumprogress)
app.component('defaultprogress',Defaultprogress)
app.component('largeprogress',Largeprogress)
app.component('basictab',Basictab)
app.component('bottomtab',Bottomtab)
app.component('linetab',Linetab)
app.component('roundtab',Roundtab)
app.component('solidtab',Solidtab)
app.component('side-settings', SideSettings)
app.component('userfilter',Userfilter)

/************profile page *********/
app.component('profiletable', ProfileTable);
app.component('profiletable1', ProfileTable1);
app.component('profilecontent', ProfileContent);

/*********Modal component**********/
app.component('ticketmodal', Ticketmodal)
app.component('locationmodal', Locationmodal)
app.component('inventorymodel',InventoryModel)
app.component('signature-model',SignatureModel)
app.component('signatureedit',Signatureedit)
app.component('selectbank',SelectBank)
app.component('signature-table',SignatureTable)
app.component('invoice',Invoice)
app.component('template-invoice-tabs',Template_Invoice_Tabs)
app.component('purchase',Purchase)
app.component('receipt',Receipt)
app.component('companies-model',Companies_Model)
app.component('subscription-model',Subscription_Model)
app.component('delete-modal', DeleteModal)
app.component('customers-ledger-modal', CustomersLedgerModal)
app.component('quotationreportmodal',Quotationreportmodal)
app.component('quotationmodel',Quotationmodel)
app.component('purchasemodel',Purchasemodel)
app.component('purchasereturnmodel',Purchasereturnmodel)
app.component('expensemodel',Expensemodel)
app.component('salesmodel',Salesmodel)
app.component('salesreturnmodel',Salesreturnmodel)
app.component('paymentmodel',Paymentmodel)
app.component('stockmodel',Stockmodel)
app.component('lowstockmodel',Lowstockmodel)
app.component('incomemodel',Incomemodel)
app.component('taxpurchasemodel',Taxpurchasemodel)
app.component('profitmodel',Profitmodel)
app.component('taxratsmodel',Taxratsmodel)
app.component('customfiledmodel',Customfiledmodel)
app.component('usermodel',Usermodel)
app.component('deleteaccountrequestmodel',Deleteaccountrequestmodel)
app.component('membershiplanmodel',Membershiplanmodel)
app.component('subscribersmodel',Subscribersmodel)
app.component('faqmodel',Faqmodel)
app.component('testimonialsmodel',Testimonialsmodel)
app.component('allblogmodel',Allblogmodel)
app.component('categoriesmodel',Categoriesmodel)
app.component('countriesmodel',Countriesmodel)
app.component('statesmodel',Statesmodel)
app.component('citiesmodel',Citiesmodel)
app.component('inactiveblogmodel', Inactiveblogmodel)
app.component('pagemodel', Pagemodel)
app.component('expenses-modal', ExpensesModal)
app.component('ticketkanban-model',Ticketkanbanmodel)
app.component('contactdetails-model',Contactdetailsmodel)
app.component('ledger-modal',Ledgermodal)
app.component('packages-modal',Packages_Modal)
app.component('seo-settings-modal',Seo_Settings_Modal)
app.component('saas-settings-modal',Saas_Settings_Modal)
app.component('email-template-modal',Email_Template_Modal)
app.component('domain-modal',Domain_Modal)


app.component('element-breadcrumb',ElementBreadcrumb)


/******************** header *************/
app.component('quotationreport-header',Quotationreportheader)
app.component('paymentreport-header',Paymentreportheader)
app.component('taxpurchase-header',Taxpurchaseheader)
app.component('profitlosslist-header',Profitlosslistheader)

/*********Dashboard**********/
app.component('index-page',DashboardPage)

app.component('vue-select', VueSelect);
app.component('date-picker', DatePicker);
app.component('vue3-autocounter', Vue3Autocounter)
app.component(VueFeather.name, VueFeather);

app.component('star-rating', StarRating)
app.use(Toaster, {
    position: "top-right",
  });
app.use(VueSweetalert2)
app.use(VueEasyLightbox);
app.use(VueApexCharts)
app.use(FlagIcon)
.use(VueFormWizard)
.use(Antd)
.use(VueTelInput)
.use(Themifyicon)
.use(SimpleLineIcons)
.use(BootstrapVue3)
.use(BToastPlugin)

// Setup navigation guards
router.beforeEach((to, from, next) => {
  const isAuthenticated = authStore.isAuthenticated;
  
  // Routes that require authentication
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/');
  }
  // Routes for non-authenticated users (like login)
  else if (to.meta.requiresGuest && isAuthenticated) {
    next('/dashboard');
  }
  else {
    next();
  }
});

app.use(router)
app.mount('#app');

