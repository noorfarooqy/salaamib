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
                  :class="currentPath == 'credit-notes' ? 'active' : 'notactive'"
                  to="credit-notes"
                  >All</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'credit-notes-pending' ? 'active' : 'notactive'"
                  to="credit-notes-pending"
                  >Pending</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'credit-notes-overdue' ? 'active' : 'notactive'"
                  to="credit-notes-overdue"
                  >Overdue</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'credit-notes-draft' ? 'active' : 'notactive'"
                  to="credit-notes-draft"
                  >Draft</router-link
                >
              </li>
              <li>
                <router-link
                  :class="
                    currentPath == 'credit-notes-recurring' ? 'active' : 'notactive'
                  "
                  to="credit-notes-recurring"
                  >Recurring</router-link
                >
              </li>
              <li>
                <router-link
                  :class="
                    currentPath == 'credit-notes-cancelled' ? 'active' : 'notactive'
                  "
                  to="credit-notes-cancelled"
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
