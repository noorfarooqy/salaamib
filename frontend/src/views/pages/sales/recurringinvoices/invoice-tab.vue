<template>
  <!-- All Invoice -->
  <div class="card invoices-tabs-card">
    <div class="invoices-main-tabs">
      <div class="row align-items-center">
        <div class="col-lg-12">
          <div class="invoices-tabs">
            <ul>
              <li>
                <router-link
                  :class="currentPath == 'recurring-invoices' ? 'active' : 'notactive'"
                  to="recurring-invoices"
                  >All Invoice</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring-paid' ? 'active' : 'notactive'"
                  to="recurring-paid"
                  >Paid</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring-pending' ? 'active' : 'notactive'"
                  to="recurring-pending"
                  >Pending</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring-overdue' ? 'active' : 'notactive'"
                  to="recurring-overdue"
                  >Overdue</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring-draft' ? 'active' : 'notactive'"
                  to="recurring-draft"
                  >Draft</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring' ? 'active' : 'notactive'"
                  to="recurring"
                  >Recurring</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'recurring-cancelled' ? 'active' : 'notactive'"
                  to="recurring-cancelled"
                  >Cancelled</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /All Invoice -->
</template>
<script>
export default {
  data() {
    return {};
  },
  computed: {
    currentPath() {
      return this.$route.name;
    },
  },
};
</script>
