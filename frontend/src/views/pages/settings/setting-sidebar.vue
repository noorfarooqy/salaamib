<template>
  <div class="card">
    <div class="card-body">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Settings</h5>
        </div>
      </div>
      <!-- Settings Menu -->
      <div class="widget settings-menu mb-0">
        <ul>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'settings' }"
              to="/settings/profile-settings"
              class="nav-link"
            >
              <i class="feather feather-user"></i> <span>Account Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'company-settings' }"
              to="/settings/company-settings"
              class="nav-link"
            >
              <i class="feather feather-settings"></i> <span>Company Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'invoice-settings' }"
              to="/settings/invoice-settings"
              class="nav-link"
            >
              <i class="feather feather-file"></i> <span>Invoice Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'template-invoice' }"
              to="/settings/template-invoice"
              class="nav-link"
            >
              <i class="feather feather-layers"></i> <span>Invoice Templates</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'payment-settings' }"
              to="/settings/payment-settings"
              class="nav-link"
            >
              <i class="feather feather-credit-card"></i> <span>Payment Methods</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'bank-account' }"
              to="/settings/bank-account"
              class="nav-link"
            >
              <i class="feather feather-aperture"></i> <span>Bank Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'tax-rats' }"
              to="/settings/tax-rats"
              class="nav-link"
            >
              <i class="feather feather-file-text"></i> <span>Tax Rates</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'plan-billing' }"
              to="/settings/plan-billing"
              class="nav-link"
            >
              <i class="feather feather-credit-card"></i> <span>Plan & Billing</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'two-factor' }"
              to="/settings/two-factor"
              class="nav-link"
            >
              <i class="feather feather-aperture"></i> <span>Two Factor</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'custom-filed' }"
              to="/settings/custom-filed"
              class="nav-link"
            >
              <i class="feather feather-file-text"></i> <span>Custom Fields</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'email-settings' }"
              to="/settings/email-settings"
              class="nav-link"
            >
              <i class="feather feather-mail"></i> <span>Email Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'preferences' }"
              to="/settings/preferences"
              class="nav-link"
            >
              <i class="feather feather-settings"></i> <span>Preference Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'email-template' }"
              to="/settings/email-template"
              class="nav-link"
            >
              <i class="feather feather-airplay"></i> <span>Email Templates</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'seo-settings' }"
              to="/settings/seo-settings"
              class="nav-link"
            >
              <i class="feather feather-send"></i> <span>SEO Settings</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-bind:class="{ active: currentPath == 'saas-settings' }"
              to="/settings/saas-settings"
              class="nav-link"
            >
              <i class="feather feather-target"></i> <span>SaaS Settings</span>
            </router-link>
          </li>
        </ul>
      </div>
      <!-- /Settings Menu -->
    </div>
  </div>
</template>
<script>
export default {
  computed: {
    currentPath() {
      return this.$route.name;
    },
  },
};
</script>
