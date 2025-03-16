<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Toastr</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card" id="types">
            <div class="card-header">
              <h4 class="card-title">Types</h4>
            </div>
            <div class="card-body card-buttons">
              <b-button variant="outline-success me-1 mb-1" @click="() => toast('success')">Success</b-button>
              <b-button variant="outline-info me-1 mb-1" @click="() => toast('info')">Info</b-button>
              <b-button variant="outline-warning me-1 mb-1" @click="() => toast('warning')">Warning</b-button>
              <b-button variant="outline-danger me-1 mb-1" @click="() => toast('error')">Error</b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title">Position</h4>
            </div>
            <div class="card-body card-buttons">
              <div class="row">
                <div class="col-sm-12 mb-4">
                  <h5 class="mb-3">Top Positions</h5>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('topLeft')">
                    Top Left
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('topCenter')">
                    Top Center
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('topRight')">
                    Top Right
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('topFullWidth')">
                    Top Full Width
                  </b-button>
                </div>

                <div class="col-sm-12">
                  <h5 class="mb-3">Bottom Positions</h5>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('bottomLeft')">
                    Bottom Left
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('bottomCenter')">
                    Bottom Center
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('bottomRight')">
                    Bottom Right
                  </b-button>
                  <b-button variant="outline-primary me-1 mb-1" @click="openNotificationTop('bottomFullWidth')">
                    Bottom Full Width
                  </b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title">Options</h4>
            </div>
            <div class="card-body card-buttons">
              <b-button variant="outline-success me-1 mb-1" @click="openNotificationWithIcon('info')">
                Notifications
              </b-button>
              <b-button variant="outline-success me-1 mb-1" @click="openNotificationWithIconclose('success')">
                Close Button
              </b-button>
              <b-button variant="outline-success me-1 mb-1" @click="openNotificationWithIconprogress('success')">
                Progress Bar
              </b-button>
              <b-button variant="outline-success me-1 mb-1" @click="openNotificationWithIconclear('info')">
                Clear Toast
              </b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title">Clear Toasts</h4>
            </div>
            <div class="card-body card-buttons">
              <div class="row mt-1">
                <div class="col-md-6 col-sm-12 mb-3 mb-md-0">
                  <h5>Remove</h5>
                  <p>Immediately remove current toasts without using animation.</p>
                  <b-button variant="outline-info me-1 mb-1" @click="() => toast('info')">
                    Show Toast
                  </b-button>
                  <b-button variant="outline-danger me-1 mb-1" @click="() => toast('error')">
                    Remove Toast
                  </b-button>
                </div>
                <div class="col-md-6 col-sm-12 mb-3 mb-md-0">
                  <h5>Clear</h5>
                  <p>Remove current toasts using animation.</p>
                  <b-button variant="outline-info me-1 mb-1" @click="() => toast('info')">
                    Show Toast
                  </b-button>
                  <b-button variant="outline-danger me-1 mb-1" @click="() => toast('error')">
                    Clear Toast
                  </b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title">Duration & Timeout</h4>
            </div>
            <div class="card-body card-buttons">
              <p>
                you can use options like <code>showDuration</code>,
                <code>hideDuration</code>, <code>timeout</code> for your toasts. To
                create a sticky toast set the <code>timeout</code> to <code>0</code>
              </p>
              <b-button variant="outline-info me-1 mb-1" @click="() => toast('success')">
                Show .5s
              </b-button>
              <b-button variant="outline-info me-1 mb-1" @click="() => toast('warning')">
                Hide 3s
              </b-button>
              <b-button variant="outline-info me-1 mb-1" @click="() => toast('error')">
                Timeout 5s
              </b-button>
              <b-button variant="outline-info me-1 mb-1" @click="() => toast('info')">
                Sticky Toast
              </b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import { notification } from "ant-design-vue";

export default {
  data() {
    return {
      message: `<span><b>Miracle Max Says</b></span><span>Have fun storming the castle!</span>`,
      options: {
        duration: 3000,
      },
      title: "Toastr",
    };
  },
  computed: {
    positions(Positions) {
      return Object.keys(Positions).map((key) => {
        return {
          key,
          value: Positions[key],
          name: Positions[key].replace(/-/, " "),
        };
      });
    },
    hasOptions() {
      return (
        this.options &&
        (Object.keys(this.options).length > 1 || this.options.duration !== 3000)
      );
    },
  },
  setup() {
    const openNotificationWithIcon = (type) => {
      notification[type]({
        message: "Miracle Max Says",
        description: "Have fun storming the castle!",
      });
    };
    const openNotificationTop = (placement) => {
      notification.open({
        message: `${placement}`,
        description: "I do not think that word means what you think it means.",
        placement,
      });
    };
    const openNotificationWithIconclose = (type) => {
      notification[type]({
        message: "With Close Button",
        description: "Have fun storming the castle!",
      });
    };
    const openNotificationWithIconprogress = (type) => {
      notification[type]({
        message: "Progress Bar",
        description: "Have fun storming the castle!",
      });
    };
    const openNotificationWithIconclear = (type) => {
      notification[type]({
        message: "Clear Toast Button",
        description: "Clear",
      });
    };
    return {
      openNotificationWithIcon,
      openNotificationTop,
      openNotificationWithIconclose,
      openNotificationWithIconprogress,
      openNotificationWithIconclear,
    };
  },
  methods: {
    openNotification(options) {
      this.$notification.open(options);
      this.nState = JSON.stringify(options, null, 2);
    },
    toast(type = "default", dismissible = true) {
      const options = {
        dismissible,
        onClick: this.onClick,
      };
      typeof type === "string" && (options.type = type);

      typeof this.options.maxToasts === "string" &&
        (this.options.maxToasts = parseInt(this.options.maxToasts));

      this.$toast.show(this.message, {
        ...options,
        ...this.options,
      });
    },
    changeDuration(e) {
      this.options.duration = !e.target.checked ? 3000 : false;
    },
    onClick(e) {
      console.log(e);
    },
  },
};
</script>
