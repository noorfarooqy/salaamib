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
                    currentPath == 'tickets-kanban' || currentPath == 'tickets'
                      ? 'active'
                      : 'notactive'"
                  to="/tickets/tickets-kanban"
                  >All</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-list-open' ? 'active' : 'notactive'"
                  to="/tickets/tickets-list-open"
                  >Open</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-list-resolved' ? 'active' : 'notactive'"
                  to="/tickets/tickets-list-resolved"
                  >Resolved</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-list-pending' ? 'active' : 'notactive'"
                  to="/tickets/tickets-list-pending"
                  >Pending</router-link
                >
              </li>
              <li>
                <router-link
                  :class="currentPath == 'tickets-list-closed' ? 'active' : 'notactive'"
                  to="/tickets/tickets-list-closed"
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
