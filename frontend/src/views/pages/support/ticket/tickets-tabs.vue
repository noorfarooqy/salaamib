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
                  :class="
                    currentPath == 'tickets' || currentPath == 'tickets-list'
                      ? 'active'
                      : 'notactive'"
                  to="/tickets/all-tickets"
                  >All</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-open' ? 'active' : 'notactive'"
                  to="/tickets/tickets-open"
                  >Open</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-resolved' ? 'active' : 'notactive'"
                  to="/tickets/tickets-resolved"
                  >Resolved</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-pending' ? 'active' : 'notactive'"
                  to="/tickets/tickets-pending"
                  >Pending</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-closed' ? 'active' : 'notactive'"
                  to="/tickets/tickets-closed"
                  >Closed</router-link
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
